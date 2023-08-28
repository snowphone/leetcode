from re import compile
from collections import deque

r"""
<expr>          ::= ( <repeated_expr> | <str> )+
<repeated_expr> ::= <num> '[' <expr> ']'
<num>           ::= \d+
<str>           ::= [a-z]+
"""


class IExpr:
    def __init__(self, tokens: deque[str]):
        self.tokens = tokens

    def eval(self) -> str:
        ...


class Str(IExpr):
    def eval(self):
        return self.tokens.popleft()


class Number(IExpr):
    def eval(self):
        return int(self.tokens.popleft())


class RepeatedStr(IExpr):
    def eval(self):
        num = Number(self.tokens).eval()
        self.tokens.popleft()  # [
        expr = Expr(self.tokens).eval()
        self.tokens.popleft()  # ]
        return num * expr


class Expr(IExpr):
    def eval(self):
        stk = []
        while self.tokens:
            token = self.tokens[0]
            if token.isdecimal():
                stk.append(RepeatedStr(self.tokens).eval())
            elif token.isalpha():
                stk.append(Str(self.tokens).eval())
            else:
                break
        return "".join(stk)


class Solution:
    token_pattern = compile(r"\d+|\[|\]|[a-z]+")

    def decodeString(self, s: str) -> str:
        tokens = deque(it.group() for it in self.token_pattern.finditer(s))
        return Expr(tokens).eval()
