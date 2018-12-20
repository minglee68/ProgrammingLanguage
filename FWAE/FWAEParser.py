# Generated from FWAE.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(")\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\5\2 \n\2\3\2\3\2\7\2$\n\2\f\2\16\2\'\13\2\3")
        buf.write("\2\2\3\2\3\2\2\2\2.\2\37\3\2\2\2\4\5\b\2\1\2\5 \7\b\2")
        buf.write("\2\6 \7\7\2\2\7\b\7\t\2\2\b\t\5\2\2\2\t\n\5\2\2\b\n \3")
        buf.write("\2\2\2\13\f\7\n\2\2\f\r\5\2\2\2\r\16\5\2\2\7\16 \3\2\2")
        buf.write("\2\17\20\7\3\2\2\20\21\7\4\2\2\21\22\7\7\2\2\22\23\5\2")
        buf.write("\2\2\23\24\7\5\2\2\24\25\5\2\2\6\25 \3\2\2\2\26\27\7\4")
        buf.write("\2\2\27\30\5\2\2\2\30\31\7\5\2\2\31 \3\2\2\2\32\33\7\6")
        buf.write("\2\2\33\34\7\4\2\2\34\35\7\7\2\2\35\36\7\5\2\2\36 \5\2")
        buf.write("\2\4\37\4\3\2\2\2\37\6\3\2\2\2\37\7\3\2\2\2\37\13\3\2")
        buf.write("\2\2\37\17\3\2\2\2\37\26\3\2\2\2\37\32\3\2\2\2 %\3\2\2")
        buf.write("\2!\"\f\3\2\2\"$\5\2\2\4#!\3\2\2\2$\'\3\2\2\2%#\3\2\2")
        buf.write("\2%&\3\2\2\2&\3\3\2\2\2\'%\3\2\2\2\4\37%")
        return buf.getvalue()


class FWAEParser ( Parser ):

    grammarFileName = "FWAE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'with'", "'{'", "'}'", "'fun'", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "ADD", "SUB", "WHITESPACE" ]

    RULE_fwae = 0

    ruleNames =  [ "fwae" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    NUM=6
    ADD=7
    SUB=8
    WHITESPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FwaeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FWAEParser.RULE_fwae

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(FWAEParser.ADD, 0)
        def fwae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FWAEParser.FwaeContext)
            else:
                return self.getTypedRuleContext(FWAEParser.FwaeContext,i)


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


    class AppContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fwae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FWAEParser.FwaeContext)
            else:
                return self.getTypedRuleContext(FWAEParser.FwaeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApp" ):
                listener.enterApp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApp" ):
                listener.exitApp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApp" ):
                return visitor.visitApp(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(FWAEParser.SUB, 0)
        def fwae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FWAEParser.FwaeContext)
            else:
                return self.getTypedRuleContext(FWAEParser.FwaeContext,i)


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


    class WithContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FWAEParser.ID, 0)
        def fwae(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FWAEParser.FwaeContext)
            else:
                return self.getTypedRuleContext(FWAEParser.FwaeContext,i)


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


    class NumContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(FWAEParser.NUM, 0)

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


    class ExprContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fwae(self):
            return self.getTypedRuleContext(FWAEParser.FwaeContext,0)


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


    class IdContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FWAEParser.ID, 0)

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


    class FunContext(FwaeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FWAEParser.FwaeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FWAEParser.ID, 0)
        def fwae(self):
            return self.getTypedRuleContext(FWAEParser.FwaeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun" ):
                listener.enterFun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun" ):
                listener.exitFun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun" ):
                return visitor.visitFun(self)
            else:
                return visitor.visitChildren(self)



    def fwae(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FWAEParser.FwaeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_fwae, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FWAEParser.NUM]:
                localctx = FWAEParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(FWAEParser.NUM)
                pass
            elif token in [FWAEParser.ID]:
                localctx = FWAEParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(FWAEParser.ID)
                pass
            elif token in [FWAEParser.ADD]:
                localctx = FWAEParser.AddContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(FWAEParser.ADD)
                self.state = 6
                self.fwae(0)
                self.state = 7
                self.fwae(6)
                pass
            elif token in [FWAEParser.SUB]:
                localctx = FWAEParser.SubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(FWAEParser.SUB)
                self.state = 10
                self.fwae(0)
                self.state = 11
                self.fwae(5)
                pass
            elif token in [FWAEParser.T__0]:
                localctx = FWAEParser.WithContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(FWAEParser.T__0)
                self.state = 14
                self.match(FWAEParser.T__1)
                self.state = 15
                self.match(FWAEParser.ID)
                self.state = 16
                self.fwae(0)
                self.state = 17
                self.match(FWAEParser.T__2)
                self.state = 18
                self.fwae(4)
                pass
            elif token in [FWAEParser.T__1]:
                localctx = FWAEParser.ExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(FWAEParser.T__1)
                self.state = 21
                self.fwae(0)
                self.state = 22
                self.match(FWAEParser.T__2)
                pass
            elif token in [FWAEParser.T__3]:
                localctx = FWAEParser.FunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(FWAEParser.T__3)
                self.state = 25
                self.match(FWAEParser.T__1)
                self.state = 26
                self.match(FWAEParser.ID)
                self.state = 27
                self.match(FWAEParser.T__2)
                self.state = 28
                self.fwae(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = FWAEParser.AppContext(self, FWAEParser.FwaeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_fwae)
                    self.state = 31
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 32
                    self.fwae(2) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.fwae_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def fwae_sempred(self, localctx:FwaeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




