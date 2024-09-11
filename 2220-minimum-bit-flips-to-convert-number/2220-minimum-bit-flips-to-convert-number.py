class Solution:
    def bitcount(self, n: int):
        cnt = 0
        for i in range(32):
            cnt += bool(n & (1 << i))
        return cnt
    def minBitFlips(self, start: int, goal: int) -> int:
        diff = start ^ goal
        return self.bitcount(diff)