class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def popcnt(n):
            return sum(bool(n & (1 << i)) for i in range(32))
        return n > 0 and popcnt(n) == 1