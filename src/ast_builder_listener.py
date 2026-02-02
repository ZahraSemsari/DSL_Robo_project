from __future__ import annotations

from typing import Any, Dict, List, Optional
from antlr4 import ParseTreeWalker

from src.ast import (
    Span,
    Program, RobotDecl, SensorDecl, ActuatorDecl, VarDecl,
    BehaviorDecl, StateDecl, Block,
    Stmt, TransitionStmt, AssignStmt, ActionStmt,
    Expr, LiteralExpr, IdExpr, UnaryExpr, BinaryExpr,
)

from src.generated.RobotDSLParser import RobotDSLParser
from src.generated.RobotDSLListener import RobotDSLListener


def _span(ctx) -> Span:
    # ctx.start موجود است
    return Span(line=ctx.start.line, col=ctx.start.column)


class ASTBuilderListener(RobotDSLListener):
    """
    Build AST using ctx->node map.
    """

    def __init__(self) -> None:
        self.node: Dict[Any, Any] = {}
        self.program: Optional[Program] = None

        self._robot_sensors: List[SensorDecl] = []
        self._robot_actuators: List[ActuatorDecl] = []
        self._robot_vars: List[VarDecl] = []
        self._robot_behaviors: List[BehaviorDecl] = []

        self._behavior_initial: Optional[str] = None

    # ---------- program / robot ----------

    def exitProgram(self, ctx: RobotDSLParser.ProgramContext):
        robot = self.node[ctx.robotDecl()]
        self.program = Program(robot=robot, span=_span(ctx))
        self.node[ctx] = self.program

    def enterRobotDecl(self, ctx: RobotDSLParser.RobotDeclContext):
        self._robot_sensors = []
        self._robot_actuators = []
        self._robot_vars = []
        self._robot_behaviors = []

    def exitRobotDecl(self, ctx: RobotDSLParser.RobotDeclContext):
        r = RobotDecl(
            name=ctx.ID().getText(),
            sensors=self._robot_sensors,
            actuators=self._robot_actuators,
            vars=self._robot_vars,
            behaviors=self._robot_behaviors,
            span=_span(ctx),
        )
        self.node[ctx] = r

    # ---------- decls ----------

    def exitSensorDecl(self, ctx: RobotDSLParser.SensorDeclContext):
        s = SensorDecl(
            name=ctx.ID().getText(),
            data_type=ctx.dataType().getText(),
            span=_span(ctx),
        )
        self.node[ctx] = s
        self._robot_sensors.append(s)

    def exitActuatorDecl(self, ctx: RobotDSLParser.ActuatorDeclContext):
        a = ActuatorDecl(
            name=ctx.ID(0).getText(),
            kind=ctx.ID(1).getText(),
            span=_span(ctx),
        )
        self.node[ctx] = a
        self._robot_actuators.append(a)

    def exitVarDecl(self, ctx: RobotDSLParser.VarDeclContext):
        init = self.node[ctx.expr()] if ctx.expr() else None
        v = VarDecl(
            name=ctx.ID().getText(),
            data_type=ctx.dataType().getText(),
            init=init,
            span=_span(ctx),
        )
        self.node[ctx] = v
        self._robot_vars.append(v)

    # ---------- behavior / states ----------

    def enterBehaviorDecl(self, ctx: RobotDSLParser.BehaviorDeclContext):
        self._behavior_initial = None

    def exitInitialDecl(self, ctx: RobotDSLParser.InitialDeclContext):
        self._behavior_initial = ctx.ID().getText()

    def exitBehaviorDecl(self, ctx: RobotDSLParser.BehaviorDeclContext):
        states: List[StateDecl] = [self.node[sctx] for sctx in ctx.stateDecl()]
        b = BehaviorDecl(
            name=ctx.ID().getText(),
            initial_state=self._behavior_initial or "",
            states=states,
            span=_span(ctx),
        )
        self.node[ctx] = b
        self._robot_behaviors.append(b)

    def exitStateDecl(self, ctx: RobotDSLParser.StateDeclContext):
        name = ctx.ID().getText()
        body = ctx.stateBody()

        enter_blk = self.node[body.enterBlock().block()] if body.enterBlock() else None
        update_blk = self.node[body.updateBlock().block()] if body.updateBlock() else None
        exit_blk = self.node[body.exitBlock().block()] if body.exitBlock() else None

        st = StateDecl(
            name=name,
            enter_on=enter_blk,
            update_on=update_blk,
            exit_on=exit_blk,
            span=_span(ctx),
        )
        self.node[ctx] = st

    # ---------- blocks / statements ----------

    def exitBlock(self, ctx: RobotDSLParser.BlockContext):
        stmts: List[Stmt] = []
        for sctx in ctx.stmt():
            st = self.node.get(sctx, None)
            if st is not None:
                stmts.append(st)
        self.node[ctx] = Block(statements=stmts, span=_span(ctx))

    def exitStmt(self, ctx: RobotDSLParser.StmtContext):
        if ctx.transitionStmt():
            self.node[ctx] = self.node[ctx.transitionStmt()]
        elif ctx.assignStmt():
            self.node[ctx] = self.node[ctx.assignStmt()]
        elif ctx.actionStmt():
            self.node[ctx] = self.node[ctx.actionStmt()]
        # else: SEMI تنها => ignore

    def exitTransitionStmt(self, ctx: RobotDSLParser.TransitionStmtContext):
        self.node[ctx] = TransitionStmt(
            cond=self.node[ctx.expr()],
            target_state=ctx.ID().getText(),
            span=_span(ctx),
        )

    def exitAssignStmt(self, ctx: RobotDSLParser.AssignStmtContext):
        self.node[ctx] = AssignStmt(
            name=ctx.ID().getText(),
            value=self.node[ctx.expr()],
            span=_span(ctx),
        )

    def exitArgList(self, ctx: RobotDSLParser.ArgListContext):
        self.node[ctx] = [self.node[e] for e in ctx.expr()]

    def exitActionStmt(self, ctx: RobotDSLParser.ActionStmtContext):
        args = self.node[ctx.argList()] if ctx.argList() else []
        self.node[ctx] = ActionStmt(
            actuator=ctx.ID(0).getText(),
            method=ctx.ID(1).getText(),
            args=args,
            span=_span(ctx),
        )

    # ---------- expressions ----------

    def exitLiteral(self, ctx: RobotDSLParser.LiteralContext):
        if ctx.BOOL_LIT():
            v = True if ctx.BOOL_LIT().getText() == "true" else False
        elif ctx.FLOAT_LIT():
            v = float(ctx.FLOAT_LIT().getText())
        elif ctx.INT_LIT():
            v = int(ctx.INT_LIT().getText())
        else:
            raw = ctx.STRING_LIT().getText()
            v = raw[1:-1]
        self.node[ctx] = LiteralExpr(value=v, span=_span(ctx))

    def exitPrimary(self, ctx: RobotDSLParser.PrimaryContext):
        if ctx.literal():
            self.node[ctx] = self.node[ctx.literal()]
        elif ctx.ID():
            self.node[ctx] = IdExpr(name=ctx.ID().getText(), span=_span(ctx))
        else:
            self.node[ctx] = self.node[ctx.expr()]

    def exitUnary(self, ctx: RobotDSLParser.UnaryContext):
        if ctx.primary():
            self.node[ctx] = self.node[ctx.primary()]
        else:
            op = ctx.getChild(0).getText()
            right = self.node[ctx.unary()]
            self.node[ctx] = UnaryExpr(op=op, right=right, span=_span(ctx))

    def _fold(self, ctx, term_ctxs: List[Any]):
        # ctx children look like: term op term op term ...
        if len(term_ctxs) == 1:
            self.node[ctx] = self.node[term_ctxs[0]]
            return

        left: Expr = self.node[term_ctxs[0]]
        for i in range(1, len(term_ctxs)):
            op_text = ctx.getChild(2 * i - 1).getText()
            right: Expr = self.node[term_ctxs[i]]
            left = BinaryExpr(left=left, op=op_text, right=right, span=_span(ctx))
        self.node[ctx] = left

    def exitMultiplication(self, ctx: RobotDSLParser.MultiplicationContext):
        self._fold(ctx, list(ctx.unary()))

    def exitAddition(self, ctx: RobotDSLParser.AdditionContext):
        self._fold(ctx, list(ctx.multiplication()))

    def exitComparison(self, ctx: RobotDSLParser.ComparisonContext):
        self._fold(ctx, list(ctx.addition()))

    def exitEquality(self, ctx: RobotDSLParser.EqualityContext):
        self._fold(ctx, list(ctx.comparison()))

    def exitLogicAnd(self, ctx: RobotDSLParser.LogicAndContext):
        self._fold(ctx, list(ctx.equality()))

    def exitLogicOr(self, ctx: RobotDSLParser.LogicOrContext):
        self._fold(ctx, list(ctx.logicAnd()))

    def exitExpr(self, ctx: RobotDSLParser.ExprContext):
        self.node[ctx] = self.node[ctx.logicOr()]


def build_ast(parse_tree) -> Program:
    listener = ASTBuilderListener()
    ParseTreeWalker().walk(listener, parse_tree)
    assert listener.program is not None
    return listener.program
