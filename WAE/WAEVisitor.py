# Generated from WAE.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WAEParser import WAEParser
else:
    from WAEParser import WAEParser

# This class defines a complete generic visitor for a parse tree produced by WAEParser.

class WAEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WAEParser#num.
    def visitNum(self, ctx:WAEParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WAEParser#id.
    def visitId(self, ctx:WAEParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WAEParser#add.
    def visitAdd(self, ctx:WAEParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WAEParser#sub.
    def visitSub(self, ctx:WAEParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WAEParser#with.
    def visitWith(self, ctx:WAEParser.WithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WAEParser#expr.
    def visitExpr(self, ctx:WAEParser.ExprContext):
        return self.visitChildren(ctx)



del WAEParser