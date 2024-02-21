from functools import reduce

class Solution:
    def bits(self, num: int):
        answer = []
        for i in range(32):
            answer.append(int(bool(num & (1 << i) )))
        return answer[::-1]
    
    def common(self, lhs, rhs):
        answer = lhs.copy()
        i = next( (i for i in range(32) if lhs[i] != rhs[i]), 32)

        for j in range(i, 32):
            answer[j] = 0
        return answer
    
    def to_dec(self, bits):
        n = 0
        for i in range(32):
            if bits[31 - i]:
                n |= (1 << i)
        return n

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lhs = self.bits(left)
        rhs = self.bits(right)

        ans = self.common(lhs, rhs)
        return self.to_dec(ans)
