import sys
from antlr4 import *
from AELexer import AELexer
from AEParser import AEParser
from MyVisitor import MyVisitor


def main(argv):
    user_input = input()
    antlr_input = InputStream(user_input)
    lexer = AELexer(antlr_input)
    stream = CommonTokenStream(lexer)
    parser = AEParser(stream)
    tree = parser.ae()
    print(tree.toStringTree(recog=parser))

    visitor = MyVisitor()
    value = visitor.visit(tree)
    print(value)

if __name__ == '__main__':
    main(sys.argv)
