# Generated from FWAE.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FWAEParser import FWAEParser
else:
    from FWAEParser import FWAEParser

# This class defines a complete generic visitor for a parse tree produced by FWAEParser.

class FWAEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FWAEParser#add.
    def visitAdd(self, ctx:FWAEParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#app.
    def visitApp(self, ctx:FWAEParser.AppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#sub.
    def visitSub(self, ctx:FWAEParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#with.
    def visitWith(self, ctx:FWAEParser.WithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#num.
    def visitNum(self, ctx:FWAEParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#expr.
    def visitExpr(self, ctx:FWAEParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#id.
    def visitId(self, ctx:FWAEParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FWAEParser#fun.
    def visitFun(self, ctx:FWAEParser.FunContext):
        return self.visitChildren(ctx)



del FWAEParser