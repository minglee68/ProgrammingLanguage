grammar FWAE;

/*
 * Parser Rules
 */

fwae : NUM # num
    | ID # id
    | '+' fwae fwae # add
    | '-' fwae fwae # sub
    | 'with' '{' ID fwae '}' fwae # with
    | '{' fwae '}' # expr
    | 'fun' '{' ID '}' fwae # fun
    | fwae fwae # app
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
