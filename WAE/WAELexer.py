# Generated from WAE.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7&\n\7\r\7\16")
        buf.write("\7\'\3\b\6\b+\n\b\r\b\16\b,\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\2\2\f\3\3\5\4\7\5\t\2\13\2\r\6\17\7\21\b\23")
        buf.write("\t\25\n\3\2\4\4\2C\\c|\3\2\62;\2\65\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\34\3\2\2\2")
        buf.write("\7\36\3\2\2\2\t \3\2\2\2\13\"\3\2\2\2\r%\3\2\2\2\17*\3")
        buf.write("\2\2\2\21.\3\2\2\2\23\60\3\2\2\2\25\62\3\2\2\2\27\30\7")
        buf.write("y\2\2\30\31\7k\2\2\31\32\7v\2\2\32\33\7j\2\2\33\4\3\2")
        buf.write("\2\2\34\35\7}\2\2\35\6\3\2\2\2\36\37\7\177\2\2\37\b\3")
        buf.write("\2\2\2 !\t\2\2\2!\n\3\2\2\2\"#\t\3\2\2#\f\3\2\2\2$&\5")
        buf.write("\t\5\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\16")
        buf.write("\3\2\2\2)+\5\13\6\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-\20\3\2\2\2./\7-\2\2/\22\3\2\2\2\60\61\7/\2\2\61")
        buf.write("\24\3\2\2\2\62\63\7\"\2\2\63\64\3\2\2\2\64\65\b\13\2\2")
        buf.write("\65\26\3\2\2\2\5\2\',\3\b\2\2")
        return buf.getvalue()


class WAELexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    NUM = 5
    ADD = 6
    SUB = 7
    WHITESPACE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'with'", "'{'", "'}'", "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "ADD", "SUB", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "LETTER", "DIGIT", "ID", "NUM", 
                  "ADD", "SUB", "WHITESPACE" ]

    grammarFileName = "WAE.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


