import operator as op

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(reduce(op.mul, map(int, [num1, num2])))