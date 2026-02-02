grammar RobotDSL;

/* ---------------- Parser Rules ---------------- */

program
  : robotDecl EOF
  ;

robotDecl
  : ROBOT ID LBRACE robotBody RBRACE
  ;

robotBody
  : sensorsBlock? actuatorsBlock? varsBlock? behaviorDecl+
  ;

sensorsBlock
  : SENSORS LBRACE sensorDecl* RBRACE
  ;

sensorDecl
  : SENSOR ID COLON dataType SEMI
  ;

actuatorsBlock
  : ACTUATORS LBRACE actuatorDecl* RBRACE
  ;

actuatorDecl
  : ACTUATOR ID COLON ID SEMI
  ;

varsBlock
  : VARS LBRACE varDecl* RBRACE
  ;

varDecl
  : VAR ID COLON dataType (ASSIGN expr)? SEMI
  ;

behaviorDecl
  : BEHAVIOR ID LBRACE initialDecl stateDecl+ RBRACE
  ;

initialDecl
  : INITIAL ID SEMI
  ;

stateDecl
  : STATE ID LBRACE stateBody RBRACE
  ;

stateBody
  : enterBlock? updateBlock? exitBlock?
  ;

enterBlock
  : ENTER_ON block
  ;

updateBlock
  : UPDATE_ON block
  ;

exitBlock
  : EXIT_ON block
  ;

block
  : LBRACE stmt* RBRACE
  ;

stmt
  : transitionStmt
  | assignStmt
  | actionStmt
  | SEMI
  ;

transitionStmt
  : IF LPAREN expr RPAREN GOTO ID SEMI
  ;

assignStmt
  : ID ASSIGN expr SEMI
  ;

actionStmt
  : ID DOT ID LPAREN argList? RPAREN SEMI
  ;

argList
  : expr (COMMA expr)*
  ;

/* Expression precedence (lowest -> highest) */
expr        : logicOr ;
logicOr     : logicAnd (OR logicAnd)* ;
logicAnd    : equality (AND equality)* ;
equality    : comparison ((EQ | NEQ) comparison)* ;
comparison  : addition ((LT | LE | GT | GE) addition)* ;
addition    : multiplication ((PLUS | MINUS) multiplication)* ;
multiplication : unary ((MUL | DIV | MOD) unary)* ;
unary
  : (NOT | PLUS | MINUS) unary
  | primary
  ;
primary
  : literal
  | ID
  | LPAREN expr RPAREN
  ;
literal
  : BOOL_LIT
  | FLOAT_LIT
  | INT_LIT
  | STRING_LIT
  ;

dataType
  : BOOL
  | INT
  | FLOAT
  | STRING
  | ID
  ;

/* ---------------- Lexer Rules ---------------- */

/* Keywords */
ROBOT      : 'robot';
SENSORS    : 'sensors';
SENSOR     : 'sensor';
ACTUATORS  : 'actuators';
ACTUATOR   : 'actuator';
VARS       : 'vars';
VAR        : 'var';
BEHAVIOR   : 'behavior';
INITIAL    : 'initial';
STATE      : 'state';
ENTER_ON   : 'enter_on';
UPDATE_ON  : 'update_on';
EXIT_ON    : 'exit_on';
IF         : 'if';
GOTO       : 'goto';

/* Types */
BOOL       : 'bool';
INT        : 'int';
FLOAT      : 'float';
STRING     : 'string';

/* Operators / punctuation */
EQ         : '==';
NEQ        : '!=';
LE         : '<=';
GE         : '>=';
LT         : '<';
GT         : '>';
ASSIGN     : '=';
PLUS       : '+';
MINUS      : '-';
MUL        : '*';
DIV        : '/';
MOD        : '%';

AND        : '&&' | 'and';
OR         : '||' | 'or';
NOT        : '!'  | 'not';

LPAREN     : '(';
RPAREN     : ')';
LBRACE     : '{';
RBRACE     : '}';
SEMI       : ';';
COLON      : ':';
COMMA      : ',';
DOT        : '.';

/* Literals */
BOOL_LIT   : 'true' | 'false';
FLOAT_LIT  : [0-9]+ '.' [0-9]+ ;
INT_LIT    : [0-9]+ ;
STRING_LIT : '"' ( ~["\\] | '\\' . )* '"' ;

/* Identifier */
ID         : [a-zA-Z_] [a-zA-Z0-9_]* ;

/* Whitespace & comments */
WS            : [ \t\r\n]+ -> skip ;
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
