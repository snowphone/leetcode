from dataclasses import dataclass
import operator
import re
from typing import Protocol, TypeGuard


class IValue(Protocol):

    def get(self) -> int:
        ...


@dataclass(unsafe_hash=True)
class Int(IValue):
    n: int

    def get(self):
        return self.n


@dataclass(unsafe_hash=True)
class Op:
    op: str
    lhs: IValue
    rhs: IValue

    def get(self):
        fn = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }[self.op]
        return fn(self.lhs.get(), self.rhs.get())


class Solution:

    def diffWaysToCompute(self, expression: str) -> list[int]:

        def mapper(x: str):
            if x not in '+-*':
                return Int(n=int(x))
            return x

        pattern = re.compile(r"[-+*]|\d+")
        tokens = [
            mapper(token.group()) for token in pattern.finditer(expression)
        ]
        return [it.get() for it in self._solve(tokens)]  # type: ignore

    def _solve(self, tokens: list[IValue | str]) -> set[IValue]:
        n = len(tokens)

        def only_value(tokens: list[IValue | str]) -> TypeGuard[list[IValue]]:
            return len(tokens) == 1

        if only_value(tokens):
            return set(tokens)

        answer = set()
        for i in range(0, n - 2, 2):
            lhs: IValue = tokens[i]  # type: ignore
            op: str = tokens[i + 1]  # type: ignore
            rhs: IValue = tokens[i + 2]  # type: ignore

            answer |= self._solve([
                *tokens[:i],
                Op(op=op, lhs=lhs, rhs=rhs),
                *tokens[i + 3:],
            ])
        return answer