# Generated from D:/4041/compiler/DSL_Robo_project/grammar/RobotDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,294,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,2,77,8,2,1,2,3,2,80,8,2,1,
        2,3,2,83,8,2,1,2,4,2,86,8,2,11,2,12,2,87,1,3,1,3,1,3,5,3,93,8,3,
        10,3,12,3,96,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,
        109,8,5,10,5,12,5,112,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,5,7,125,8,7,10,7,12,7,128,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,138,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,4,9,147,8,9,11,9,12,
        9,148,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,3,12,164,8,12,1,12,3,12,167,8,12,1,12,3,12,170,8,12,1,13,1,
        13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,5,16,183,8,16,10,
        16,12,16,186,9,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,194,8,17,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,
        20,1,20,1,20,1,20,1,20,3,20,214,8,20,1,20,1,20,1,20,1,21,1,21,1,
        21,5,21,222,8,21,10,21,12,21,225,9,21,1,22,1,22,1,23,1,23,1,23,5,
        23,232,8,23,10,23,12,23,235,9,23,1,24,1,24,1,24,5,24,240,8,24,10,
        24,12,24,243,9,24,1,25,1,25,1,25,5,25,248,8,25,10,25,12,25,251,9,
        25,1,26,1,26,1,26,5,26,256,8,26,10,26,12,26,259,9,26,1,27,1,27,1,
        27,5,27,264,8,27,10,27,12,27,267,9,27,1,28,1,28,1,28,5,28,272,8,
        28,10,28,12,28,275,9,28,1,29,1,29,1,29,3,29,280,8,29,1,30,1,30,1,
        30,1,30,1,30,1,30,3,30,288,8,30,1,31,1,31,1,32,1,32,1,32,0,0,33,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,0,7,1,0,20,21,1,0,22,25,1,0,27,28,
        1,0,29,31,2,0,27,28,34,34,1,0,43,46,2,0,16,19,47,47,287,0,66,1,0,
        0,0,2,69,1,0,0,0,4,76,1,0,0,0,6,89,1,0,0,0,8,99,1,0,0,0,10,105,1,
        0,0,0,12,115,1,0,0,0,14,121,1,0,0,0,16,131,1,0,0,0,18,141,1,0,0,
        0,20,152,1,0,0,0,22,156,1,0,0,0,24,163,1,0,0,0,26,171,1,0,0,0,28,
        174,1,0,0,0,30,177,1,0,0,0,32,180,1,0,0,0,34,193,1,0,0,0,36,195,
        1,0,0,0,38,203,1,0,0,0,40,208,1,0,0,0,42,218,1,0,0,0,44,226,1,0,
        0,0,46,228,1,0,0,0,48,236,1,0,0,0,50,244,1,0,0,0,52,252,1,0,0,0,
        54,260,1,0,0,0,56,268,1,0,0,0,58,279,1,0,0,0,60,287,1,0,0,0,62,289,
        1,0,0,0,64,291,1,0,0,0,66,67,3,2,1,0,67,68,5,0,0,1,68,1,1,0,0,0,
        69,70,5,1,0,0,70,71,5,47,0,0,71,72,5,37,0,0,72,73,3,4,2,0,73,74,
        5,38,0,0,74,3,1,0,0,0,75,77,3,6,3,0,76,75,1,0,0,0,76,77,1,0,0,0,
        77,79,1,0,0,0,78,80,3,10,5,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,
        0,0,0,81,83,3,14,7,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,
        86,3,18,9,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,
        0,0,88,5,1,0,0,0,89,90,5,2,0,0,90,94,5,37,0,0,91,93,3,8,4,0,92,91,
        1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,
        96,94,1,0,0,0,97,98,5,38,0,0,98,7,1,0,0,0,99,100,5,3,0,0,100,101,
        5,47,0,0,101,102,5,40,0,0,102,103,3,64,32,0,103,104,5,39,0,0,104,
        9,1,0,0,0,105,106,5,4,0,0,106,110,5,37,0,0,107,109,3,12,6,0,108,
        107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,
        113,1,0,0,0,112,110,1,0,0,0,113,114,5,38,0,0,114,11,1,0,0,0,115,
        116,5,5,0,0,116,117,5,47,0,0,117,118,5,40,0,0,118,119,5,47,0,0,119,
        120,5,39,0,0,120,13,1,0,0,0,121,122,5,6,0,0,122,126,5,37,0,0,123,
        125,3,16,8,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,
        127,1,0,0,0,127,129,1,0,0,0,128,126,1,0,0,0,129,130,5,38,0,0,130,
        15,1,0,0,0,131,132,5,7,0,0,132,133,5,47,0,0,133,134,5,40,0,0,134,
        137,3,64,32,0,135,136,5,26,0,0,136,138,3,44,22,0,137,135,1,0,0,0,
        137,138,1,0,0,0,138,139,1,0,0,0,139,140,5,39,0,0,140,17,1,0,0,0,
        141,142,5,8,0,0,142,143,5,47,0,0,143,144,5,37,0,0,144,146,3,20,10,
        0,145,147,3,22,11,0,146,145,1,0,0,0,147,148,1,0,0,0,148,146,1,0,
        0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,5,38,0,0,151,19,1,0,
        0,0,152,153,5,9,0,0,153,154,5,47,0,0,154,155,5,39,0,0,155,21,1,0,
        0,0,156,157,5,10,0,0,157,158,5,47,0,0,158,159,5,37,0,0,159,160,3,
        24,12,0,160,161,5,38,0,0,161,23,1,0,0,0,162,164,3,26,13,0,163,162,
        1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,167,3,28,14,0,166,165,
        1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,170,3,30,15,0,169,168,
        1,0,0,0,169,170,1,0,0,0,170,25,1,0,0,0,171,172,5,11,0,0,172,173,
        3,32,16,0,173,27,1,0,0,0,174,175,5,12,0,0,175,176,3,32,16,0,176,
        29,1,0,0,0,177,178,5,13,0,0,178,179,3,32,16,0,179,31,1,0,0,0,180,
        184,5,37,0,0,181,183,3,34,17,0,182,181,1,0,0,0,183,186,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,
        188,5,38,0,0,188,33,1,0,0,0,189,194,3,36,18,0,190,194,3,38,19,0,
        191,194,3,40,20,0,192,194,5,39,0,0,193,189,1,0,0,0,193,190,1,0,0,
        0,193,191,1,0,0,0,193,192,1,0,0,0,194,35,1,0,0,0,195,196,5,14,0,
        0,196,197,5,35,0,0,197,198,3,44,22,0,198,199,5,36,0,0,199,200,5,
        15,0,0,200,201,5,47,0,0,201,202,5,39,0,0,202,37,1,0,0,0,203,204,
        5,47,0,0,204,205,5,26,0,0,205,206,3,44,22,0,206,207,5,39,0,0,207,
        39,1,0,0,0,208,209,5,47,0,0,209,210,5,42,0,0,210,211,5,47,0,0,211,
        213,5,35,0,0,212,214,3,42,21,0,213,212,1,0,0,0,213,214,1,0,0,0,214,
        215,1,0,0,0,215,216,5,36,0,0,216,217,5,39,0,0,217,41,1,0,0,0,218,
        223,3,44,22,0,219,220,5,41,0,0,220,222,3,44,22,0,221,219,1,0,0,0,
        222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,43,1,0,0,0,225,
        223,1,0,0,0,226,227,3,46,23,0,227,45,1,0,0,0,228,233,3,48,24,0,229,
        230,5,33,0,0,230,232,3,48,24,0,231,229,1,0,0,0,232,235,1,0,0,0,233,
        231,1,0,0,0,233,234,1,0,0,0,234,47,1,0,0,0,235,233,1,0,0,0,236,241,
        3,50,25,0,237,238,5,32,0,0,238,240,3,50,25,0,239,237,1,0,0,0,240,
        243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,49,1,0,0,0,243,241,
        1,0,0,0,244,249,3,52,26,0,245,246,7,0,0,0,246,248,3,52,26,0,247,
        245,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        51,1,0,0,0,251,249,1,0,0,0,252,257,3,54,27,0,253,254,7,1,0,0,254,
        256,3,54,27,0,255,253,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,
        258,1,0,0,0,258,53,1,0,0,0,259,257,1,0,0,0,260,265,3,56,28,0,261,
        262,7,2,0,0,262,264,3,56,28,0,263,261,1,0,0,0,264,267,1,0,0,0,265,
        263,1,0,0,0,265,266,1,0,0,0,266,55,1,0,0,0,267,265,1,0,0,0,268,273,
        3,58,29,0,269,270,7,3,0,0,270,272,3,58,29,0,271,269,1,0,0,0,272,
        275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,57,1,0,0,0,275,273,
        1,0,0,0,276,277,7,4,0,0,277,280,3,58,29,0,278,280,3,60,30,0,279,
        276,1,0,0,0,279,278,1,0,0,0,280,59,1,0,0,0,281,288,3,62,31,0,282,
        288,5,47,0,0,283,284,5,35,0,0,284,285,3,44,22,0,285,286,5,36,0,0,
        286,288,1,0,0,0,287,281,1,0,0,0,287,282,1,0,0,0,287,283,1,0,0,0,
        288,61,1,0,0,0,289,290,7,5,0,0,290,63,1,0,0,0,291,292,7,6,0,0,292,
        65,1,0,0,0,24,76,79,82,87,94,110,126,137,148,163,166,169,184,193,
        213,223,233,241,249,257,265,273,279,287
    ]

class RobotDSLParser ( Parser ):

    grammarFileName = "RobotDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'robot'", "'sensors'", "'sensor'", "'actuators'", 
                     "'actuator'", "'vars'", "'var'", "'behavior'", "'initial'", 
                     "'state'", "'enter_on'", "'update_on'", "'exit_on'", 
                     "'if'", "'goto'", "'bool'", "'int'", "'float'", "'string'", 
                     "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "':'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "ROBOT", "SENSORS", "SENSOR", "ACTUATORS", 
                      "ACTUATOR", "VARS", "VAR", "BEHAVIOR", "INITIAL", 
                      "STATE", "ENTER_ON", "UPDATE_ON", "EXIT_ON", "IF", 
                      "GOTO", "BOOL", "INT", "FLOAT", "STRING", "EQ", "NEQ", 
                      "LE", "GE", "LT", "GT", "ASSIGN", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "AND", "OR", "NOT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMI", "COLON", "COMMA", 
                      "DOT", "BOOL_LIT", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
                      "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_robotDecl = 1
    RULE_robotBody = 2
    RULE_sensorsBlock = 3
    RULE_sensorDecl = 4
    RULE_actuatorsBlock = 5
    RULE_actuatorDecl = 6
    RULE_varsBlock = 7
    RULE_varDecl = 8
    RULE_behaviorDecl = 9
    RULE_initialDecl = 10
    RULE_stateDecl = 11
    RULE_stateBody = 12
    RULE_enterBlock = 13
    RULE_updateBlock = 14
    RULE_exitBlock = 15
    RULE_block = 16
    RULE_stmt = 17
    RULE_transitionStmt = 18
    RULE_assignStmt = 19
    RULE_actionStmt = 20
    RULE_argList = 21
    RULE_expr = 22
    RULE_logicOr = 23
    RULE_logicAnd = 24
    RULE_equality = 25
    RULE_comparison = 26
    RULE_addition = 27
    RULE_multiplication = 28
    RULE_unary = 29
    RULE_primary = 30
    RULE_literal = 31
    RULE_dataType = 32

    ruleNames =  [ "program", "robotDecl", "robotBody", "sensorsBlock", 
                   "sensorDecl", "actuatorsBlock", "actuatorDecl", "varsBlock", 
                   "varDecl", "behaviorDecl", "initialDecl", "stateDecl", 
                   "stateBody", "enterBlock", "updateBlock", "exitBlock", 
                   "block", "stmt", "transitionStmt", "assignStmt", "actionStmt", 
                   "argList", "expr", "logicOr", "logicAnd", "equality", 
                   "comparison", "addition", "multiplication", "unary", 
                   "primary", "literal", "dataType" ]

    EOF = Token.EOF
    ROBOT=1
    SENSORS=2
    SENSOR=3
    ACTUATORS=4
    ACTUATOR=5
    VARS=6
    VAR=7
    BEHAVIOR=8
    INITIAL=9
    STATE=10
    ENTER_ON=11
    UPDATE_ON=12
    EXIT_ON=13
    IF=14
    GOTO=15
    BOOL=16
    INT=17
    FLOAT=18
    STRING=19
    EQ=20
    NEQ=21
    LE=22
    GE=23
    LT=24
    GT=25
    ASSIGN=26
    PLUS=27
    MINUS=28
    MUL=29
    DIV=30
    MOD=31
    AND=32
    OR=33
    NOT=34
    LPAREN=35
    RPAREN=36
    LBRACE=37
    RBRACE=38
    SEMI=39
    COLON=40
    COMMA=41
    DOT=42
    BOOL_LIT=43
    FLOAT_LIT=44
    INT_LIT=45
    STRING_LIT=46
    ID=47
    WS=48
    LINE_COMMENT=49
    BLOCK_COMMENT=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def robotDecl(self):
            return self.getTypedRuleContext(RobotDSLParser.RobotDeclContext,0)


        def EOF(self):
            return self.getToken(RobotDSLParser.EOF, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RobotDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.robotDecl()
            self.state = 67
            self.match(RobotDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RobotDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROBOT(self):
            return self.getToken(RobotDSLParser.ROBOT, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def robotBody(self):
            return self.getTypedRuleContext(RobotDSLParser.RobotBodyContext,0)


        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_robotDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRobotDecl" ):
                listener.enterRobotDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRobotDecl" ):
                listener.exitRobotDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRobotDecl" ):
                return visitor.visitRobotDecl(self)
            else:
                return visitor.visitChildren(self)




    def robotDecl(self):

        localctx = RobotDSLParser.RobotDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_robotDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(RobotDSLParser.ROBOT)
            self.state = 70
            self.match(RobotDSLParser.ID)
            self.state = 71
            self.match(RobotDSLParser.LBRACE)
            self.state = 72
            self.robotBody()
            self.state = 73
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RobotBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sensorsBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.SensorsBlockContext,0)


        def actuatorsBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.ActuatorsBlockContext,0)


        def varsBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.VarsBlockContext,0)


        def behaviorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.BehaviorDeclContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.BehaviorDeclContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_robotBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRobotBody" ):
                listener.enterRobotBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRobotBody" ):
                listener.exitRobotBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRobotBody" ):
                return visitor.visitRobotBody(self)
            else:
                return visitor.visitChildren(self)




    def robotBody(self):

        localctx = RobotDSLParser.RobotBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_robotBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 75
                self.sensorsBlock()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 78
                self.actuatorsBlock()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 81
                self.varsBlock()


            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.behaviorDecl()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SensorsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENSORS(self):
            return self.getToken(RobotDSLParser.SENSORS, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def sensorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.SensorDeclContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.SensorDeclContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_sensorsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSensorsBlock" ):
                listener.enterSensorsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSensorsBlock" ):
                listener.exitSensorsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSensorsBlock" ):
                return visitor.visitSensorsBlock(self)
            else:
                return visitor.visitChildren(self)




    def sensorsBlock(self):

        localctx = RobotDSLParser.SensorsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sensorsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(RobotDSLParser.SENSORS)
            self.state = 90
            self.match(RobotDSLParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 91
                self.sensorDecl()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SensorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENSOR(self):
            return self.getToken(RobotDSLParser.SENSOR, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def COLON(self):
            return self.getToken(RobotDSLParser.COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(RobotDSLParser.DataTypeContext,0)


        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_sensorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSensorDecl" ):
                listener.enterSensorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSensorDecl" ):
                listener.exitSensorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSensorDecl" ):
                return visitor.visitSensorDecl(self)
            else:
                return visitor.visitChildren(self)




    def sensorDecl(self):

        localctx = RobotDSLParser.SensorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sensorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(RobotDSLParser.SENSOR)
            self.state = 100
            self.match(RobotDSLParser.ID)
            self.state = 101
            self.match(RobotDSLParser.COLON)
            self.state = 102
            self.dataType()
            self.state = 103
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActuatorsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTUATORS(self):
            return self.getToken(RobotDSLParser.ACTUATORS, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def actuatorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.ActuatorDeclContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.ActuatorDeclContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_actuatorsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActuatorsBlock" ):
                listener.enterActuatorsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActuatorsBlock" ):
                listener.exitActuatorsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActuatorsBlock" ):
                return visitor.visitActuatorsBlock(self)
            else:
                return visitor.visitChildren(self)




    def actuatorsBlock(self):

        localctx = RobotDSLParser.ActuatorsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actuatorsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(RobotDSLParser.ACTUATORS)
            self.state = 106
            self.match(RobotDSLParser.LBRACE)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 107
                self.actuatorDecl()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActuatorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTUATOR(self):
            return self.getToken(RobotDSLParser.ACTUATOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.ID)
            else:
                return self.getToken(RobotDSLParser.ID, i)

        def COLON(self):
            return self.getToken(RobotDSLParser.COLON, 0)

        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_actuatorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActuatorDecl" ):
                listener.enterActuatorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActuatorDecl" ):
                listener.exitActuatorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActuatorDecl" ):
                return visitor.visitActuatorDecl(self)
            else:
                return visitor.visitChildren(self)




    def actuatorDecl(self):

        localctx = RobotDSLParser.ActuatorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actuatorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(RobotDSLParser.ACTUATOR)
            self.state = 116
            self.match(RobotDSLParser.ID)
            self.state = 117
            self.match(RobotDSLParser.COLON)
            self.state = 118
            self.match(RobotDSLParser.ID)
            self.state = 119
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARS(self):
            return self.getToken(RobotDSLParser.VARS, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.VarDeclContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_varsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsBlock" ):
                listener.enterVarsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsBlock" ):
                listener.exitVarsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarsBlock" ):
                return visitor.visitVarsBlock(self)
            else:
                return visitor.visitChildren(self)




    def varsBlock(self):

        localctx = RobotDSLParser.VarsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(RobotDSLParser.VARS)
            self.state = 122
            self.match(RobotDSLParser.LBRACE)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 123
                self.varDecl()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RobotDSLParser.VAR, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def COLON(self):
            return self.getToken(RobotDSLParser.COLON, 0)

        def dataType(self):
            return self.getTypedRuleContext(RobotDSLParser.DataTypeContext,0)


        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(RobotDSLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RobotDSLParser.ExprContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = RobotDSLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(RobotDSLParser.VAR)
            self.state = 132
            self.match(RobotDSLParser.ID)
            self.state = 133
            self.match(RobotDSLParser.COLON)
            self.state = 134
            self.dataType()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 135
                self.match(RobotDSLParser.ASSIGN)
                self.state = 136
                self.expr()


            self.state = 139
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BehaviorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEHAVIOR(self):
            return self.getToken(RobotDSLParser.BEHAVIOR, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def initialDecl(self):
            return self.getTypedRuleContext(RobotDSLParser.InitialDeclContext,0)


        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def stateDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.StateDeclContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.StateDeclContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_behaviorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBehaviorDecl" ):
                listener.enterBehaviorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBehaviorDecl" ):
                listener.exitBehaviorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBehaviorDecl" ):
                return visitor.visitBehaviorDecl(self)
            else:
                return visitor.visitChildren(self)




    def behaviorDecl(self):

        localctx = RobotDSLParser.BehaviorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_behaviorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(RobotDSLParser.BEHAVIOR)
            self.state = 142
            self.match(RobotDSLParser.ID)
            self.state = 143
            self.match(RobotDSLParser.LBRACE)
            self.state = 144
            self.initialDecl()
            self.state = 146 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 145
                self.stateDecl()
                self.state = 148 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 150
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INITIAL(self):
            return self.getToken(RobotDSLParser.INITIAL, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_initialDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialDecl" ):
                listener.enterInitialDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialDecl" ):
                listener.exitInitialDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialDecl" ):
                return visitor.visitInitialDecl(self)
            else:
                return visitor.visitChildren(self)




    def initialDecl(self):

        localctx = RobotDSLParser.InitialDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initialDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(RobotDSLParser.INITIAL)
            self.state = 153
            self.match(RobotDSLParser.ID)
            self.state = 154
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self):
            return self.getToken(RobotDSLParser.STATE, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def stateBody(self):
            return self.getTypedRuleContext(RobotDSLParser.StateBodyContext,0)


        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_stateDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDecl" ):
                listener.enterStateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDecl" ):
                listener.exitStateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDecl" ):
                return visitor.visitStateDecl(self)
            else:
                return visitor.visitChildren(self)




    def stateDecl(self):

        localctx = RobotDSLParser.StateDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stateDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(RobotDSLParser.STATE)
            self.state = 157
            self.match(RobotDSLParser.ID)
            self.state = 158
            self.match(RobotDSLParser.LBRACE)
            self.state = 159
            self.stateBody()
            self.state = 160
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enterBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.EnterBlockContext,0)


        def updateBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.UpdateBlockContext,0)


        def exitBlock(self):
            return self.getTypedRuleContext(RobotDSLParser.ExitBlockContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_stateBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateBody" ):
                listener.enterStateBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateBody" ):
                listener.exitStateBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateBody" ):
                return visitor.visitStateBody(self)
            else:
                return visitor.visitChildren(self)




    def stateBody(self):

        localctx = RobotDSLParser.StateBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stateBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 162
                self.enterBlock()


            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 165
                self.updateBlock()


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 168
                self.exitBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnterBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTER_ON(self):
            return self.getToken(RobotDSLParser.ENTER_ON, 0)

        def block(self):
            return self.getTypedRuleContext(RobotDSLParser.BlockContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_enterBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnterBlock" ):
                listener.enterEnterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnterBlock" ):
                listener.exitEnterBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnterBlock" ):
                return visitor.visitEnterBlock(self)
            else:
                return visitor.visitChildren(self)




    def enterBlock(self):

        localctx = RobotDSLParser.EnterBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_enterBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(RobotDSLParser.ENTER_ON)
            self.state = 172
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE_ON(self):
            return self.getToken(RobotDSLParser.UPDATE_ON, 0)

        def block(self):
            return self.getTypedRuleContext(RobotDSLParser.BlockContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_updateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateBlock" ):
                listener.enterUpdateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateBlock" ):
                listener.exitUpdateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateBlock" ):
                return visitor.visitUpdateBlock(self)
            else:
                return visitor.visitChildren(self)




    def updateBlock(self):

        localctx = RobotDSLParser.UpdateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_updateBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(RobotDSLParser.UPDATE_ON)
            self.state = 175
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT_ON(self):
            return self.getToken(RobotDSLParser.EXIT_ON, 0)

        def block(self):
            return self.getTypedRuleContext(RobotDSLParser.BlockContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_exitBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExitBlock" ):
                listener.enterExitBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExitBlock" ):
                listener.exitExitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExitBlock" ):
                return visitor.visitExitBlock(self)
            else:
                return visitor.visitChildren(self)




    def exitBlock(self):

        localctx = RobotDSLParser.ExitBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exitBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(RobotDSLParser.EXIT_ON)
            self.state = 178
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(RobotDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RobotDSLParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.StmtContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.StmtContext,i)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = RobotDSLParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(RobotDSLParser.LBRACE)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141287244185600) != 0):
                self.state = 181
                self.stmt()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(RobotDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transitionStmt(self):
            return self.getTypedRuleContext(RobotDSLParser.TransitionStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(RobotDSLParser.AssignStmtContext,0)


        def actionStmt(self):
            return self.getTypedRuleContext(RobotDSLParser.ActionStmtContext,0)


        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = RobotDSLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.transitionStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.actionStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(RobotDSLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransitionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RobotDSLParser.IF, 0)

        def LPAREN(self):
            return self.getToken(RobotDSLParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(RobotDSLParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(RobotDSLParser.RPAREN, 0)

        def GOTO(self):
            return self.getToken(RobotDSLParser.GOTO, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_transitionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitionStmt" ):
                listener.enterTransitionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitionStmt" ):
                listener.exitTransitionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransitionStmt" ):
                return visitor.visitTransitionStmt(self)
            else:
                return visitor.visitChildren(self)




    def transitionStmt(self):

        localctx = RobotDSLParser.TransitionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_transitionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(RobotDSLParser.IF)
            self.state = 196
            self.match(RobotDSLParser.LPAREN)
            self.state = 197
            self.expr()
            self.state = 198
            self.match(RobotDSLParser.RPAREN)
            self.state = 199
            self.match(RobotDSLParser.GOTO)
            self.state = 200
            self.match(RobotDSLParser.ID)
            self.state = 201
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(RobotDSLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RobotDSLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = RobotDSLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(RobotDSLParser.ID)
            self.state = 204
            self.match(RobotDSLParser.ASSIGN)
            self.state = 205
            self.expr()
            self.state = 206
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.ID)
            else:
                return self.getToken(RobotDSLParser.ID, i)

        def DOT(self):
            return self.getToken(RobotDSLParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(RobotDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RobotDSLParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(RobotDSLParser.SEMI, 0)

        def argList(self):
            return self.getTypedRuleContext(RobotDSLParser.ArgListContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_actionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionStmt" ):
                listener.enterActionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionStmt" ):
                listener.exitActionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionStmt" ):
                return visitor.visitActionStmt(self)
            else:
                return visitor.visitChildren(self)




    def actionStmt(self):

        localctx = RobotDSLParser.ActionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_actionStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(RobotDSLParser.ID)
            self.state = 209
            self.match(RobotDSLParser.DOT)
            self.state = 210
            self.match(RobotDSLParser.ID)
            self.state = 211
            self.match(RobotDSLParser.LPAREN)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 272730825949184) != 0):
                self.state = 212
                self.argList()


            self.state = 215
            self.match(RobotDSLParser.RPAREN)
            self.state = 216
            self.match(RobotDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.COMMA)
            else:
                return self.getToken(RobotDSLParser.COMMA, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = RobotDSLParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.expr()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 219
                self.match(RobotDSLParser.COMMA)
                self.state = 220
                self.expr()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOr(self):
            return self.getTypedRuleContext(RobotDSLParser.LogicOrContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = RobotDSLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.logicOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.LogicAndContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.LogicAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.OR)
            else:
                return self.getToken(RobotDSLParser.OR, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_logicOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)




    def logicOr(self):

        localctx = RobotDSLParser.LogicOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logicOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.logicAnd()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 229
                self.match(RobotDSLParser.OR)
                self.state = 230
                self.logicAnd()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.EqualityContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.AND)
            else:
                return self.getToken(RobotDSLParser.AND, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_logicAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicAnd(self):

        localctx = RobotDSLParser.LogicAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_logicAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.equality()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 237
                self.match(RobotDSLParser.AND)
                self.state = 238
                self.equality()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.ComparisonContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.EQ)
            else:
                return self.getToken(RobotDSLParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.NEQ)
            else:
                return self.getToken(RobotDSLParser.NEQ, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = RobotDSLParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.comparison()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.comparison()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.AdditionContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.AdditionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.LT)
            else:
                return self.getToken(RobotDSLParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.LE)
            else:
                return self.getToken(RobotDSLParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.GT)
            else:
                return self.getToken(RobotDSLParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.GE)
            else:
                return self.getToken(RobotDSLParser.GE, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = RobotDSLParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.addition()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0):
                self.state = 253
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 254
                self.addition()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.MultiplicationContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.MultiplicationContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.PLUS)
            else:
                return self.getToken(RobotDSLParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.MINUS)
            else:
                return self.getToken(RobotDSLParser.MINUS, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)




    def addition(self):

        localctx = RobotDSLParser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.multiplication()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.multiplication()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotDSLParser.UnaryContext)
            else:
                return self.getTypedRuleContext(RobotDSLParser.UnaryContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.MUL)
            else:
                return self.getToken(RobotDSLParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.DIV)
            else:
                return self.getToken(RobotDSLParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(RobotDSLParser.MOD)
            else:
                return self.getToken(RobotDSLParser.MOD, i)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_multiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)




    def multiplication(self):

        localctx = RobotDSLParser.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.unary()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                self.state = 269
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 270
                self.unary()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(RobotDSLParser.UnaryContext,0)


        def NOT(self):
            return self.getToken(RobotDSLParser.NOT, 0)

        def PLUS(self):
            return self.getToken(RobotDSLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(RobotDSLParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(RobotDSLParser.PrimaryContext,0)


        def getRuleIndex(self):
            return RobotDSLParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = RobotDSLParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17582522368) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self.unary()
                pass
            elif token in [35, 43, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(RobotDSLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(RobotDSLParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(RobotDSLParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(RobotDSLParser.RPAREN, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = RobotDSLParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primary)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.literal()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(RobotDSLParser.ID)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(RobotDSLParser.LPAREN)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(RobotDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(RobotDSLParser.BOOL_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(RobotDSLParser.FLOAT_LIT, 0)

        def INT_LIT(self):
            return self.getToken(RobotDSLParser.INT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(RobotDSLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = RobotDSLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131941395333120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(RobotDSLParser.BOOL, 0)

        def INT(self):
            return self.getToken(RobotDSLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(RobotDSLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(RobotDSLParser.STRING, 0)

        def ID(self):
            return self.getToken(RobotDSLParser.ID, 0)

        def getRuleIndex(self):
            return RobotDSLParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = RobotDSLParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737489338368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





