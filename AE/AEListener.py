# Generated from AE.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AEParser import AEParser
else:
    from AEParser import AEParser

# This class defines a complete listener for a parse tree produced by AEParser.
class AEListener(ParseTreeListener):

    # Enter a parse tree produced by AEParser#num.
    def enterNum(self, ctx:AEParser.NumContext):
        pass

    # Exit a parse tree produced by AEParser#num.
    def exitNum(self, ctx:AEParser.NumContext):
        pass


    # Enter a parse tree produced by AEParser#id.
    def enterId(self, ctx:AEParser.IdContext):
        pass

    # Exit a parse tree produced by AEParser#id.
    def exitId(self, ctx:AEParser.IdContext):
        pass


    # Enter a parse tree produced by AEParser#add.
    def enterAdd(self, ctx:AEParser.AddContext):
        pass

    # Exit a parse tree produced by AEParser#add.
    def exitAdd(self, ctx:AEParser.AddContext):
        pass


    # Enter a parse tree produced by AEParser#sub.
    def enterSub(self, ctx:AEParser.SubContext):
        pass

    # Exit a parse tree produced by AEParser#sub.
    def exitSub(self, ctx:AEParser.SubContext):
        pass


