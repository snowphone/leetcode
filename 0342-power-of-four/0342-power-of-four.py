class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        def getbit(n: int, i: int):
            return n & (1 << i)

        if n <= 0:
            return False
        if n == 1:
            return True
        if n & 1:
            return False

        return all(not getbit(n, i) for i in range(1, 32, 2) ) and sum(1 for i in range(2, 32, 2) if getbit(n, i) ) == 1
        