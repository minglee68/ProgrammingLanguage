from WAEVisitor import WAEVisitor
from WAEParser import WAEParser

class MyVisitor(WAEVisitor):
    def __init__(self):
        self.memory = {}
        self.withcount = {}

    def visitExpr(self, ctx):
        return self.visit(ctx.wae())

    def visitNum(self, ctx):
        return ctx.NUM().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name][self.withcount[name]]
        return name

    def visitAdd(self, ctx):
        try:
            left = int(self.visit(ctx.wae(0)))
            right = int(self.visit(ctx.wae(1)))
            return left + right
        except ValueError as e:
            print("Free identifier error!")


    def visitSub(self, ctx):
        left = int(self.visit(ctx.wae(0)))
        right = int(self.visit(ctx.wae(1)))
        return left - right

    def visitWith(self, ctx):
        name = ctx.ID().getText()
        value = ctx.wae(0)
        expr = ctx.wae(1)
        return self.subst(expr, name, value)

    def subst(self, expr, name, value):
        if isinstance(expr, WAEParser.NumContext):
            return self.visit(expr)
        if isinstance(expr, WAEParser.IdContext):
            if expr.ID().getText() == name:
                return int(self.visit(value))
        if isinstance(expr, WAEParser.AddContext):
            left = int(self.subst(expr.wae(0), name, value))
            right = int(self.subst(expr.wae(1), name, value))
            return left + right
        if isinstance(expr, WAEParser.SubContext):
            left = int(self.subst(expr.wae(0), name, value))
            right = int(self.subst(expr.wae(1), name, value))
            return left - right
        if isinstance(expr, WAEParser.WithContext):
            withname = expr.ID().getText()
            withvalue = self.subst(expr.wae(0), name, value)
            if withname == name:
                withexpr = expr.wae(1)
            else:
                withexpr = self.subst(expr.wae(1), name, value)
            return self.subst(withexpr, withname, withvalue) 
        if isinstance(expr, WAEParser.WaeContext):
            return self.subst(expr.wae(), name, value)
        if isinstance(expr, WAEParser.ExprContext):
            return self.subst(expr.wae(), name, value)
