Sintactical rules:


program ::= stmt PROGRAM_OUT.

assignstmt ::= IDENTIFIER "==" expression

expression ::= expression "+" term | term

type1 ::= "BOOL" | "CHAR" | "INT" | "STRING"

arraydecl ::= "VECTOR" "[" nr "]"  type1

type  ::= type1|arraydecl

stmtlist ::= stmt | stmt ":*" stmtlist

stmt ::= simplstmt | structstmt

simplstmt ::= assignstmt | iostmt

iostmt ::= "read" | "write" "(" IDENTIFIER ")"

term ::= term "*" factor | factor

ifstmt ::= "is" "(" condition ")""?" "{" stmt ":*" "} "isnot" "{" stmt ":*" "}"

whilestmt ::= "while" "(" condition ")" "{" stmt ":*" "}"

condition ::= expression RELATION expression

RELATION ::= "<" | "<=" | "==" | "!==" | ">=" | ">" | ?