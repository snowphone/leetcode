from math import gcd, lcm
import re

class Fraction:
    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        return
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def parse(s: str):
        pass

    def __add__(self, rhs):
        lhs = self

        denom = lcm(lhs.denominator, rhs.denominator)
        lmult = denom // lhs.denominator
        rmult = denom // rhs.denominator
        numer = lmult * lhs.numerator + rmult * rhs.numerator

        return Fraction(numer, denom).reduced()
    
    def __sub__(self, rhs):
        rhs.numerator *= -1
        return self + rhs
    
    def reduced(self):
        common = gcd(self.numerator, self.denominator)

        return Fraction(self.numerator // common, self.denominator // common)
    
def parse(s):
    """
    expr ::= num | binop
    num ::= [0-9]+ | '-' [0-9]+
    binop ::== frac [+-] frac
    frac ::= num '/' num
    """
    tokenpattern = re.compile(r"\d+|[/+-]")
    tokens = [it.group() for it in tokenpattern.finditer(s)]
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
            stk.append('/')
        else:
            rhs = int(token)
            if stk and stk[-1] == '/':
               op = stk.pop()
               lhs = stk.pop()
               stk.append(Fraction(lhs, rhs)) 
            else:
                stk.append(rhs)
        i += 1
        
    # Calc
    stk, tokens = [], stk
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '-':
            i += 1
            next_token = tokens[i]
            stk[-1] = stk[-1] - next_token
        elif token == '+':
            i += 1
            next_token = tokens[i]
            stk[-1] = stk[-1] + next_token
        else:
            stk.append(token)
        i += 1

    return stk[-1]

class Solution:
    def fractionAddition(self, expression: str) -> str:
        return str(parse(expression))