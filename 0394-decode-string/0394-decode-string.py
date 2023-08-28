from re import compile
from collections import deque


# expr := (num '[' expr ']' | str)+
# num := \d+
# str := [a-z]+


class INode:
    def __init__(self, tokens: deque[str]):
        self.tokens = tokens

    def execute(self):
        ...


class Str(INode):
    def execute(self):
        return self.tokens.popleft()


class Number(INode):
    def execute(self):
        return int(self.tokens.popleft())

class Expr(INode):
    def execute(self):
        stk = []
        while self.tokens:
            token = self.tokens[0]
            if token.isdecimal():
                node = Number(self.tokens)
                stk.append(node.execute())
            elif token == "[":
                self.tokens.popleft()
                node = Expr(self.tokens)
                stk[-1] = stk[-1] * node.execute()
            elif token == "]":
                self.tokens.popleft()
                break
            else:  # str
                stk.append(Str(self.tokens).execute())
        return "".join(stk)


class Solution:
    token_pattern = compile(r"\d+|\[|\]|[a-z]+")

    def decodeString(self, s: str) -> str:
        tokens = deque(it.group() for it in self.token_pattern.finditer(s))
        exprs = []
        while tokens:
            exprs.append(Expr(tokens).execute())
        return "".join(exprs)