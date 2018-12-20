# Generated from AE.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AEParser import AEParser
else:
    from AEParser import AEParser

# This class defines a complete generic visitor for a parse tree produced by AEParser.

class AEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AEParser#num.
    def visitNum(self, ctx:AEParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AEParser#id.
    def visitId(self, ctx:AEParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AEParser#add.
    def visitAdd(self, ctx:AEParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AEParser#sub.
    def visitSub(self, ctx:AEParser.SubContext):
        return self.visitChildren(ctx)



del AEParser