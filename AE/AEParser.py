# Generated from AE.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\25\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\5\2\23\n\2\3\2\2\2\3\2\2\2\2\26\2\22\3")
        buf.write("\2\2\2\4\23\7\6\2\2\5\23\7\5\2\2\6\7\7\3\2\2\7\b\7\7\2")
        buf.write("\2\b\t\5\2\2\2\t\n\5\2\2\2\n\13\7\4\2\2\13\23\3\2\2\2")
        buf.write("\f\r\7\3\2\2\r\16\7\b\2\2\16\17\5\2\2\2\17\20\5\2\2\2")
        buf.write("\20\21\7\4\2\2\21\23\3\2\2\2\22\4\3\2\2\2\22\5\3\2\2\2")
        buf.write("\22\6\3\2\2\2\22\f\3\2\2\2\23\3\3\2\2\2\3\22")
        return buf.getvalue()


class AEParser ( Parser ):

    grammarFileName = "AE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "ADD", "SUB", "WHITESPACE" ]

    RULE_ae = 0

    ruleNames =  [ "ae" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    NUM=4
    ADD=5
    SUB=6
    WHITESPACE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AEParser.RULE_ae

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(AeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AEParser.AeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(AEParser.ADD, 0)
        def ae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AEParser.AeContext)
            else:
                return self.getTypedRuleContext(AEParser.AeContext,i)


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


    class SubContext(AeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AEParser.AeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(AEParser.SUB, 0)
        def ae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AEParser.AeContext)
            else:
                return self.getTypedRuleContext(AEParser.AeContext,i)


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


    class NumContext(AeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AEParser.AeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(AEParser.NUM, 0)

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


    class IdContext(AeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AEParser.AeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AEParser.ID, 0)

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



    def ae(self):

        localctx = AEParser.AeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ae)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = AEParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(AEParser.NUM)
                pass

            elif la_ == 2:
                localctx = AEParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 3
                self.match(AEParser.ID)
                pass

            elif la_ == 3:
                localctx = AEParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 4
                self.match(AEParser.T__0)
                self.state = 5
                self.match(AEParser.ADD)
                self.state = 6
                self.ae()
                self.state = 7
                self.ae()
                self.state = 8
                self.match(AEParser.T__1)
                pass

            elif la_ == 4:
                localctx = AEParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 10
                self.match(AEParser.T__0)
                self.state = 11
                self.match(AEParser.SUB)
                self.state = 12
                self.ae()
                self.state = 13
                self.ae()
                self.state = 14
                self.match(AEParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





