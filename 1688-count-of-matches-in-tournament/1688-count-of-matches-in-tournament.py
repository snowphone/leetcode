class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1:
            return n // 2 + self.numberOfMatches(n//2 + 1)
        else:
            return n // 2 + self.numberOfMatches(n // 2)