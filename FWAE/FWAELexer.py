# Generated from FWAE.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\6\b,\n\b\r\b\16\b-\3\t\6\t\61\n\t\r\t\16\t\62\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6")
        buf.write("\13\2\r\2\17\7\21\b\23\t\25\n\27\13\3\2\4\4\2C\\c|\3\2")
        buf.write("\62;\2;\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\3\31\3\2\2\2\5\36\3\2\2\2\7 \3\2\2\2\t\"")
        buf.write("\3\2\2\2\13&\3\2\2\2\r(\3\2\2\2\17+\3\2\2\2\21\60\3\2")
        buf.write("\2\2\23\64\3\2\2\2\25\66\3\2\2\2\278\3\2\2\2\31\32\7y")
        buf.write("\2\2\32\33\7k\2\2\33\34\7v\2\2\34\35\7j\2\2\35\4\3\2\2")
        buf.write("\2\36\37\7}\2\2\37\6\3\2\2\2 !\7\177\2\2!\b\3\2\2\2\"")
        buf.write("#\7h\2\2#$\7w\2\2$%\7p\2\2%\n\3\2\2\2&\'\t\2\2\2\'\f\3")
        buf.write("\2\2\2()\t\3\2\2)\16\3\2\2\2*,\5\13\6\2+*\3\2\2\2,-\3")
        buf.write("\2\2\2-+\3\2\2\2-.\3\2\2\2.\20\3\2\2\2/\61\5\r\7\2\60")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\22\3\2\2\2\64\65\7-\2\2\65\24\3\2\2\2\66\67\7/\2\2\67")
        buf.write("\26\3\2\2\289\7\"\2\29:\3\2\2\2:;\b\f\2\2;\30\3\2\2\2")
        buf.write("\5\2-\62\3\b\2\2")
        return buf.getvalue()


class FWAELexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    NUM = 6
    ADD = 7
    SUB = 8
    WHITESPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'with'", "'{'", "'}'", "'fun'", "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "ADD", "SUB", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LETTER", "DIGIT", "ID", 
                  "NUM", "ADD", "SUB", "WHITESPACE" ]

    grammarFileName = "FWAE.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


