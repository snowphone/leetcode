from dataclasses import dataclass
import operator
import re
from typing import Protocol


class Intf(Protocol):

    def get(self) -> int:
        ...


@dataclass(unsafe_hash=True)
class Val(Intf):
    n: int | Intf

    def get(self):
        if isinstance(self.n, int):
            return self.n
        return self.n.get()


@dataclass(unsafe_hash=True)
class Op:
    op: str
    lhs: Intf
    rhs: Intf

    def get(self):
        fn = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }[self.op]
        return fn(self.lhs.get(), self.rhs.get())


class Solution:

    def diffWaysToCompute(self, expression: str) -> list[int]:

        def mapper(x):
            if x not in '+-*':
                return Val(n=int(x))
            return x

        pattern = re.compile(r"[-+*]|\d+")
        tokens = [
            mapper(token.group()) for token in pattern.finditer(expression)
        ]
        return [it.get() for it in self._solve(tokens)]

    def _solve(self, tokens: list[Intf | str]) -> set[Intf]:
        n = len(tokens)

        if n == 1:
            return set(tokens)  # type: ignore

        answer = set()
        for i in range(0, n - 2, 2):
            lhs, op, rhs = tokens[i:i + 3]

            answer |= self._solve([
                *tokens[:i],
                Op(op=op, lhs=lhs, rhs=rhs),
                *tokens[i + 3:],
            ])
        return answer
