from operator import add, sub, mul
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda a, b: int(a / b),
        } 
        for token in tokens:
            if token in op.keys():
                b = stk.pop()
                a = stk.pop()
                stk.append(  op[token](a, b) )
            else:
                stk.append( int(token) )
        return stk[-1]