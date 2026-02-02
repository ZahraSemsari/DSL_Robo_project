# Generated from D:/4041/compiler/DSL_Robo_project/grammar/RobotDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RobotDSLParser import RobotDSLParser
else:
    from RobotDSLParser import RobotDSLParser

# This class defines a complete generic visitor for a parse tree produced by RobotDSLParser.

class RobotDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RobotDSLParser#program.
    def visitProgram(self, ctx:RobotDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#robotDecl.
    def visitRobotDecl(self, ctx:RobotDSLParser.RobotDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#robotBody.
    def visitRobotBody(self, ctx:RobotDSLParser.RobotBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#sensorsBlock.
    def visitSensorsBlock(self, ctx:RobotDSLParser.SensorsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#sensorDecl.
    def visitSensorDecl(self, ctx:RobotDSLParser.SensorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#actuatorsBlock.
    def visitActuatorsBlock(self, ctx:RobotDSLParser.ActuatorsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#actuatorDecl.
    def visitActuatorDecl(self, ctx:RobotDSLParser.ActuatorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#varsBlock.
    def visitVarsBlock(self, ctx:RobotDSLParser.VarsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#varDecl.
    def visitVarDecl(self, ctx:RobotDSLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#behaviorDecl.
    def visitBehaviorDecl(self, ctx:RobotDSLParser.BehaviorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#initialDecl.
    def visitInitialDecl(self, ctx:RobotDSLParser.InitialDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#stateDecl.
    def visitStateDecl(self, ctx:RobotDSLParser.StateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#stateBody.
    def visitStateBody(self, ctx:RobotDSLParser.StateBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#enterBlock.
    def visitEnterBlock(self, ctx:RobotDSLParser.EnterBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#updateBlock.
    def visitUpdateBlock(self, ctx:RobotDSLParser.UpdateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#exitBlock.
    def visitExitBlock(self, ctx:RobotDSLParser.ExitBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#block.
    def visitBlock(self, ctx:RobotDSLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#stmt.
    def visitStmt(self, ctx:RobotDSLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#transitionStmt.
    def visitTransitionStmt(self, ctx:RobotDSLParser.TransitionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#assignStmt.
    def visitAssignStmt(self, ctx:RobotDSLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#actionStmt.
    def visitActionStmt(self, ctx:RobotDSLParser.ActionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#argList.
    def visitArgList(self, ctx:RobotDSLParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#expr.
    def visitExpr(self, ctx:RobotDSLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#logicOr.
    def visitLogicOr(self, ctx:RobotDSLParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#logicAnd.
    def visitLogicAnd(self, ctx:RobotDSLParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#equality.
    def visitEquality(self, ctx:RobotDSLParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#comparison.
    def visitComparison(self, ctx:RobotDSLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#addition.
    def visitAddition(self, ctx:RobotDSLParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#multiplication.
    def visitMultiplication(self, ctx:RobotDSLParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#unary.
    def visitUnary(self, ctx:RobotDSLParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#primary.
    def visitPrimary(self, ctx:RobotDSLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#literal.
    def visitLiteral(self, ctx:RobotDSLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotDSLParser#dataType.
    def visitDataType(self, ctx:RobotDSLParser.DataTypeContext):
        return self.visitChildren(ctx)



del RobotDSLParser