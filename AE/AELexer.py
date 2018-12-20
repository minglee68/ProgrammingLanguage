# Generated from AE.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\6\6\37\n\6\r\6\16\6 \3\7\6\7$\n\7\r\7\16\7%\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\n\3\n\2\2\13\3\3\5\4\7\2\t\2\13")
        buf.write("\5\r\6\17\7\21\b\23\t\3\2\4\4\2C\\c|\3\2\62;\2.\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2")
        buf.write("\7\31\3\2\2\2\t\33\3\2\2\2\13\36\3\2\2\2\r#\3\2\2\2\17")
        buf.write("\'\3\2\2\2\21)\3\2\2\2\23+\3\2\2\2\25\26\7}\2\2\26\4\3")
        buf.write("\2\2\2\27\30\7\177\2\2\30\6\3\2\2\2\31\32\t\2\2\2\32\b")
        buf.write("\3\2\2\2\33\34\t\3\2\2\34\n\3\2\2\2\35\37\5\7\4\2\36\35")
        buf.write("\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\f\3\2\2\2")
        buf.write("\"$\5\t\5\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&")
        buf.write("\16\3\2\2\2\'(\7-\2\2(\20\3\2\2\2)*\7/\2\2*\22\3\2\2\2")
        buf.write("+,\7\"\2\2,-\3\2\2\2-.\b\n\2\2.\24\3\2\2\2\5\2 %\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class AELexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    NUM = 4
    ADD = 5
    SUB = 6
    WHITESPACE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "ADD", "SUB", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "LETTER", "DIGIT", "ID", "NUM", "ADD", 
                  "SUB", "WHITESPACE" ]

    grammarFileName = "AE.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


