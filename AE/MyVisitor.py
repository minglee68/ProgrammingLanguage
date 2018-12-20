from AEVisitor import AEVisitor
from AEParser import AEParser

class MyVisitor(AEVisitor):
    def __init__(self):
        self.memory = {}

    def visitNum(self, ctx):
        return ctx.NUM().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        return 0

    def visitAdd(self, ctx):
        left = int(self.visit(ctx.ae(0)))
        right = int(self.visit(ctx.ae(1)))
        return left + right

    def visitSub(self, ctx):
        left = int(self.visit(ctx.ae(0)))
        right = int(self.visit(ctx.ae(1)))
        return left - right
