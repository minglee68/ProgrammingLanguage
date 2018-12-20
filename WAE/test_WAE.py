import sys
from antlr4 import *
from WAELexer import WAELexer
from WAEParser import WAEParser
from MyVisitor import MyVisitor

def main():
    while(1):
        user_input = input()
        if user_input == 'quit':
            break
        antlr_input = InputStream(user_input)
        lexer = WAELexer(antlr_input)
        stream = CommonTokenStream(lexer)
        parser = WAEParser(stream)
        tree = parser.wae()
        #print(tree.toStringTree(recog=parser))

        visitor = MyVisitor()
        value = visitor.visit(tree)
        print(value)


if __name__ == '__main__':
    main()
