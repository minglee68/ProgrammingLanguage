grammar WAE;

/*
 * Parser Rules
 */

wae : NUM # num
    | ID # id
    | '+' wae wae # add
    | '-' wae wae # sub
    | 'with' '{' ID wae '}' wae # with
    | '{' wae '}' # expr
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
