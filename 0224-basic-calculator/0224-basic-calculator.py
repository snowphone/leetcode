import re
from operator import add, sub
from collections import deque

PSEUDO_EBNF = r"""
<expr>      ::= <sign_expr> ( <op> <sign_expr> )*
<op>        ::= '+' | '-'
<sign_expr> ::= ['-'] <num>
<num>       ::= \d+ | '(' <expr> ')'
"""


class IExpr:
    expr: int

    @property
    def eval(self):
        return self.expr


class NumExpr(IExpr):
    def __init__(self, tokens: deque[str]):
        token = tokens[0]
        if token == "(":
            tokens.popleft()
            self.expr = Expr(tokens).eval
            assert tokens.popleft() == ")"
        else:
            self.expr = int(tokens.popleft())
        return


class SignExpr(IExpr):
    def __init__(self, tokens: deque[str]):
        if tokens[0] == "-":
            tokens.popleft()
            self.expr = -NumExpr(tokens).eval
        else:
            self.expr = NumExpr(tokens).eval
        return


class OpExpr(IExpr):
    def __init__(self, lhs: IExpr, tokens: deque[str]):
        self.op = {"+": add, "-": sub}[tokens[0]]
        tokens.popleft()

        rhs = SignExpr(tokens)
        self.expr = self.op(lhs.eval, rhs.eval)


class Expr(IExpr):
    def __init__(self, tokens: deque[str]):
        lhs = SignExpr(tokens)
        while tokens:
            try:
                lhs = OpExpr(lhs, tokens)
            except KeyError:
                break
        self.expr = lhs.eval
        return


class Solution:
    token_pattern = re.compile(r"[+()-]|\d+")

    def calculate(self, s: str) -> int:
        tokens = deque(self.token_pattern.findall(s))
        return Expr(tokens).expr
