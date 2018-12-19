import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser


def main(argv):
    user_input = input()
    antlr_input = InputStream(user_input)
    lexer = HelloLexer(antlr_input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
