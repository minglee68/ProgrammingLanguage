# Generated from WAE.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\34\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\32\n\2")
        buf.write("\3\2\2\2\3\2\2\2\2\37\2\31\3\2\2\2\4\32\7\7\2\2\5\32\7")
        buf.write("\6\2\2\6\7\7\b\2\2\7\b\5\2\2\2\b\t\5\2\2\2\t\32\3\2\2")
        buf.write("\2\n\13\7\t\2\2\13\f\5\2\2\2\f\r\5\2\2\2\r\32\3\2\2\2")
        buf.write("\16\17\7\3\2\2\17\20\7\4\2\2\20\21\7\6\2\2\21\22\5\2\2")
        buf.write("\2\22\23\7\5\2\2\23\24\5\2\2\2\24\32\3\2\2\2\25\26\7\4")
        buf.write("\2\2\26\27\5\2\2\2\27\30\7\5\2\2\30\32\3\2\2\2\31\4\3")
        buf.write("\2\2\2\31\5\3\2\2\2\31\6\3\2\2\2\31\n\3\2\2\2\31\16\3")
        buf.write("\2\2\2\31\25\3\2\2\2\32\3\3\2\2\2\3\31")
        return buf.getvalue()


class WAEParser ( Parser ):

    grammarFileName = "WAE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'with'", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "ADD", "SUB", "WHITESPACE" ]

    RULE_wae = 0

    ruleNames =  [ "wae" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    NUM=5
    ADD=6
    SUB=7
    WHITESPACE=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WaeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WAEParser.RULE_wae

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(WAEParser.ADD, 0)
        def wae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WAEParser.WaeContext)
            else:
                return self.getTypedRuleContext(WAEParser.WaeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(WAEParser.SUB, 0)
        def wae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WAEParser.WaeContext)
            else:
                return self.getTypedRuleContext(WAEParser.WaeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class WithContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WAEParser.ID, 0)
        def wae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WAEParser.WaeContext)
            else:
                return self.getTypedRuleContext(WAEParser.WaeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWith" ):
                listener.enterWith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWith" ):
                listener.exitWith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWith" ):
                return visitor.visitWith(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(WAEParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class ExprContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def wae(self):
            return self.getTypedRuleContext(WAEParser.WaeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(WaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WAEParser.WaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WAEParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def wae(self):

        localctx = WAEParser.WaeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_wae)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WAEParser.NUM]:
                localctx = WAEParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(WAEParser.NUM)
                pass
            elif token in [WAEParser.ID]:
                localctx = WAEParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 3
                self.match(WAEParser.ID)
                pass
            elif token in [WAEParser.ADD]:
                localctx = WAEParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 4
                self.match(WAEParser.ADD)
                self.state = 5
                self.wae()
                self.state = 6
                self.wae()
                pass
            elif token in [WAEParser.SUB]:
                localctx = WAEParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 8
                self.match(WAEParser.SUB)
                self.state = 9
                self.wae()
                self.state = 10
                self.wae()
                pass
            elif token in [WAEParser.T__0]:
                localctx = WAEParser.WithContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 12
                self.match(WAEParser.T__0)
                self.state = 13
                self.match(WAEParser.T__1)
                self.state = 14
                self.match(WAEParser.ID)
                self.state = 15
                self.wae()
                self.state = 16
                self.match(WAEParser.T__2)
                self.state = 17
                self.wae()
                pass
            elif token in [WAEParser.T__1]:
                localctx = WAEParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 19
                self.match(WAEParser.T__1)
                self.state = 20
                self.wae()
                self.state = 21
                self.match(WAEParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





