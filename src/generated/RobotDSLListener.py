# Generated from D:/4041/compiler/DSL_Robo_project/grammar/RobotDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RobotDSLParser import RobotDSLParser
else:
    from RobotDSLParser import RobotDSLParser

# This class defines a complete listener for a parse tree produced by RobotDSLParser.
class RobotDSLListener(ParseTreeListener):

    # Enter a parse tree produced by RobotDSLParser#program.
    def enterProgram(self, ctx:RobotDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#program.
    def exitProgram(self, ctx:RobotDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#robotDecl.
    def enterRobotDecl(self, ctx:RobotDSLParser.RobotDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#robotDecl.
    def exitRobotDecl(self, ctx:RobotDSLParser.RobotDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#robotBody.
    def enterRobotBody(self, ctx:RobotDSLParser.RobotBodyContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#robotBody.
    def exitRobotBody(self, ctx:RobotDSLParser.RobotBodyContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#sensorsBlock.
    def enterSensorsBlock(self, ctx:RobotDSLParser.SensorsBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#sensorsBlock.
    def exitSensorsBlock(self, ctx:RobotDSLParser.SensorsBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#sensorDecl.
    def enterSensorDecl(self, ctx:RobotDSLParser.SensorDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#sensorDecl.
    def exitSensorDecl(self, ctx:RobotDSLParser.SensorDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#actuatorsBlock.
    def enterActuatorsBlock(self, ctx:RobotDSLParser.ActuatorsBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#actuatorsBlock.
    def exitActuatorsBlock(self, ctx:RobotDSLParser.ActuatorsBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#actuatorDecl.
    def enterActuatorDecl(self, ctx:RobotDSLParser.ActuatorDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#actuatorDecl.
    def exitActuatorDecl(self, ctx:RobotDSLParser.ActuatorDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#varsBlock.
    def enterVarsBlock(self, ctx:RobotDSLParser.VarsBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#varsBlock.
    def exitVarsBlock(self, ctx:RobotDSLParser.VarsBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#varDecl.
    def enterVarDecl(self, ctx:RobotDSLParser.VarDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#varDecl.
    def exitVarDecl(self, ctx:RobotDSLParser.VarDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#behaviorDecl.
    def enterBehaviorDecl(self, ctx:RobotDSLParser.BehaviorDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#behaviorDecl.
    def exitBehaviorDecl(self, ctx:RobotDSLParser.BehaviorDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#initialDecl.
    def enterInitialDecl(self, ctx:RobotDSLParser.InitialDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#initialDecl.
    def exitInitialDecl(self, ctx:RobotDSLParser.InitialDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#stateDecl.
    def enterStateDecl(self, ctx:RobotDSLParser.StateDeclContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#stateDecl.
    def exitStateDecl(self, ctx:RobotDSLParser.StateDeclContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#stateBody.
    def enterStateBody(self, ctx:RobotDSLParser.StateBodyContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#stateBody.
    def exitStateBody(self, ctx:RobotDSLParser.StateBodyContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#enterBlock.
    def enterEnterBlock(self, ctx:RobotDSLParser.EnterBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#enterBlock.
    def exitEnterBlock(self, ctx:RobotDSLParser.EnterBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#updateBlock.
    def enterUpdateBlock(self, ctx:RobotDSLParser.UpdateBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#updateBlock.
    def exitUpdateBlock(self, ctx:RobotDSLParser.UpdateBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#exitBlock.
    def enterExitBlock(self, ctx:RobotDSLParser.ExitBlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#exitBlock.
    def exitExitBlock(self, ctx:RobotDSLParser.ExitBlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#block.
    def enterBlock(self, ctx:RobotDSLParser.BlockContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#block.
    def exitBlock(self, ctx:RobotDSLParser.BlockContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#stmt.
    def enterStmt(self, ctx:RobotDSLParser.StmtContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#stmt.
    def exitStmt(self, ctx:RobotDSLParser.StmtContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#transitionStmt.
    def enterTransitionStmt(self, ctx:RobotDSLParser.TransitionStmtContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#transitionStmt.
    def exitTransitionStmt(self, ctx:RobotDSLParser.TransitionStmtContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#assignStmt.
    def enterAssignStmt(self, ctx:RobotDSLParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#assignStmt.
    def exitAssignStmt(self, ctx:RobotDSLParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#actionStmt.
    def enterActionStmt(self, ctx:RobotDSLParser.ActionStmtContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#actionStmt.
    def exitActionStmt(self, ctx:RobotDSLParser.ActionStmtContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#argList.
    def enterArgList(self, ctx:RobotDSLParser.ArgListContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#argList.
    def exitArgList(self, ctx:RobotDSLParser.ArgListContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#expr.
    def enterExpr(self, ctx:RobotDSLParser.ExprContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#expr.
    def exitExpr(self, ctx:RobotDSLParser.ExprContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#logicOr.
    def enterLogicOr(self, ctx:RobotDSLParser.LogicOrContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#logicOr.
    def exitLogicOr(self, ctx:RobotDSLParser.LogicOrContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#logicAnd.
    def enterLogicAnd(self, ctx:RobotDSLParser.LogicAndContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#logicAnd.
    def exitLogicAnd(self, ctx:RobotDSLParser.LogicAndContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#equality.
    def enterEquality(self, ctx:RobotDSLParser.EqualityContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#equality.
    def exitEquality(self, ctx:RobotDSLParser.EqualityContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#comparison.
    def enterComparison(self, ctx:RobotDSLParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#comparison.
    def exitComparison(self, ctx:RobotDSLParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#addition.
    def enterAddition(self, ctx:RobotDSLParser.AdditionContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#addition.
    def exitAddition(self, ctx:RobotDSLParser.AdditionContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#multiplication.
    def enterMultiplication(self, ctx:RobotDSLParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#multiplication.
    def exitMultiplication(self, ctx:RobotDSLParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#unary.
    def enterUnary(self, ctx:RobotDSLParser.UnaryContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#unary.
    def exitUnary(self, ctx:RobotDSLParser.UnaryContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#primary.
    def enterPrimary(self, ctx:RobotDSLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#primary.
    def exitPrimary(self, ctx:RobotDSLParser.PrimaryContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#literal.
    def enterLiteral(self, ctx:RobotDSLParser.LiteralContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#literal.
    def exitLiteral(self, ctx:RobotDSLParser.LiteralContext):
        pass


    # Enter a parse tree produced by RobotDSLParser#dataType.
    def enterDataType(self, ctx:RobotDSLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by RobotDSLParser#dataType.
    def exitDataType(self, ctx:RobotDSLParser.DataTypeContext):
        pass



del RobotDSLParser