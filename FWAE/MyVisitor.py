from FWAEVisitor import FWAEVisitor
from FWAEParser import FWAEParser

class MyVisitor(FWAEVisitor):
    def __init__(self):
        self.memory = {}
        self.withcount = {}
        self.funmemory = {}

    def visitExpr(self, ctx):
        return self.visit(ctx.fwae())

    def visitNum(self, ctx):
        return ctx.NUM().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name][self.withcount[name]]
        return name

    def visitAdd(self, ctx):
        try:
            left = int(self.visit(ctx.fwae(0)))
            right = int(self.visit(ctx.fwae(1)))
            return left + right
        except ValueError as e:
            print("Free identifier error!")


    def visitSub(self, ctx):
        try:
            left = int(self.visit(ctx.fwae(0)))
            right = int(self.visit(ctx.fwae(1)))
            return left - right
        except ValueError as e:
            print("Free identifier error!")

    def visitWith(self, ctx):
        name = ctx.ID().getText()
        value = ctx.fwae(0)
        expr = ctx.fwae(1)
        return self.subst(expr, name, value)

    def visitFun(self, ctx, *argv):
        for arg in argv:
            self.funmemory[ctx.ID().getText()] = arg
            return 0
        self.funmemory[ctx.ID().getText()] = ctx.fwae()
        return 0

    def visitApp(self, ctx, *argv):
        for arg in argv:
            if isinstance(ctx, FWAEParser.FunContext):
                print(ctx.fwae().getText())
                print(ctx.ID().getText())
                print(arg)
                return self.subst(ctx.fwae(), ctx.ID().getText(), arg)
            return ctx
        return self.subst(ctx.fwae(0).fwae(), ctx.fwae(0).ID().getText(), self.visit(ctx.fwae(1)))

    def subst(self, expr, name, value):
        if isinstance(expr, FWAEParser.NumContext):
            return self.visit(expr)
        elif isinstance(expr, FWAEParser.IdContext):
            if expr.ID().getText() == name:
                if isinstance(value, str) and value.isdecimal():
                    return int(value)
                if isinstance(value, FWAEParser.FwaeContext):
                    if isinstance(value, FWAEParser.NumContext):
                        return int(self.visit(value))
                    if isinstance(value.fwae(), FWAEParser.FunContext):
                        return value.fwae()
                return int(self.visit(value))
        elif isinstance(expr, FWAEParser.AddContext):
            try:
                left = int(self.subst(expr.fwae(0), name, value))
                right = int(self.subst(expr.fwae(1), name, value))
                return left + right
            except ValueError as e:
                print("Free identifier error!")
            except:
                print("error!")
        elif isinstance(expr, FWAEParser.SubContext):
            try:
                left = int(self.subst(expr.fwae(0), name, value))
                right = int(self.subst(expr.fwae(1), name, value))
                return left - right
            except ValueError as e:
                print("Free identifier error!")
            except:
                print("error!")
        elif isinstance(expr, FWAEParser.WithContext):
            withname = expr.ID().getText()
            withvalue = self.subst(expr.fwae(0), name, value)
            if withname == name:
                withexpr = expr.fwae(1)
            else:
                withexpr = self.subst(expr.fwae(1), name, value)
            return self.subst(withexpr, withname, withvalue) 
        elif isinstance(expr, FWAEParser.FunContext):
            if expr.ID().getText() == name:
                return self.visitFun(expr)
            else:
                return self.visitFun(expr, self.subst(expr.fwae(), name, value))
        elif isinstance(expr, FWAEParser.AppContext):
            return self.visitApp(self.subst(expr.fwae(0), name, value), self.subst(expr.fwae(1), name, value))
        elif isinstance(expr, FWAEParser.FwaeContext):
            return self.subst(expr.fwae(), name, value)
        elif isinstance(expr, FWAEParser.ExprContext):
            return self.subst(expr.fwae(), name, value)
