grammar AE;

/*
 * Parser Rules
 */

ae : NUM # num
   | ID # id
   | '{' '+' ae ae '}' # add
   | '{' '-' ae ae '}' # sub
   ;

/*
 * Lexer Rules
 */

fragment LETTER : [a-zA-Z] ;
fragment DIGIT : [0-9] ;

ID : LETTER+ ;
NUM : DIGIT+ ;
ADD : '+' ;
SUB : '-' ;


WHITESPACE: ' ' -> skip ;
