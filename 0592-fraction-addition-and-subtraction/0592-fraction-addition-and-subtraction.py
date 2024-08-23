from math import gcd, lcm
from operator import add, sub
import re

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        return
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, rhs):
        lhs = self

        denom = lcm(lhs.denominator, rhs.denominator)
        lmult = denom // lhs.denominator
        rmult = denom // rhs.denominator
        numer = lmult * lhs.numerator + rmult * rhs.numerator

        return Fraction(numer, denom).reduced()
    
    def __sub__(self, rhs):
        return self + Fraction(
            -rhs.numerator,
            rhs.denominator,
        )
    
    def reduced(self):
        common = gcd(self.numerator, self.denominator)

        return Fraction(self.numerator // common, self.denominator // common)
    
class Solution:
    def fractionAddition(self, expression: str) -> str:
        tokenpattern = re.compile(r"\d+|[/+-]")
        tokens = [it.group() for it in tokenpattern.finditer(expression)]
        stk = []
        i = 0
        # Fractionize
        while i < len(tokens):
            token = tokens[i]
            if token in ['-', '+']:
                if not stk:
                    stk.append(Fraction(0, 1))
                stk.append(token)
            elif token == '/':
                rhs = int(tokens[i+1])
                i += 1
                lhs = stk.pop()
                stk.append(Fraction(lhs, rhs)) 
            else:
                stk.append(int(token))
            i += 1
            
        # Add/sub
        stk, tokens = [], stk
        i = 0
        op = { '-': sub, '+': add }
        while i < len(tokens):
            token = tokens[i]
            if token in ['-', '+']:
                i += 1
                next_token = tokens[i]
                stk[-1] = op[token](stk[-1] , next_token)
            else:
                stk.append(token)
            i += 1
    
        return str(stk[-1])