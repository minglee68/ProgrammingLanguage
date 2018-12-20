import sys
from antlr4 import *
from FWAELexer import FWAELexer
from FWAEParser import FWAEParser
from MyVisitor import MyVisitor

def main():
    while(1):
        user_input = input()
        if user_input == 'quit':
            break
        antlr_input = InputStream(user_input)
        lexer = FWAELexer(antlr_input)
        stream = CommonTokenStream(lexer)
        parser = FWAEParser(stream)
        tree = parser.fwae()
        print(tree.toStringTree(recog=parser))

        visitor = MyVisitor()
        value = visitor.visit(tree)
        print(value)


if __name__ == '__main__':
    main()
