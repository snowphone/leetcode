class Solution:
    def shortestPalindrome(self, s: str) -> str:
        self.s = s
        n = len(s)
        return self.solve(n, n * 2)

    def is_palindrome(self, s):
        return s == s[::-1]
    
    def solve(self, min_len: int, max_len: int):
        return next(
            it for i in range(min_len, max_len + 1)
            if self.is_palindrome(it := self.make(i))
        )
    
    def make(self, sz: int):
        s = self.s
        remaining_len = sz - len(s)
        remaining = s[::-1][:remaining_len]

        return remaining + s
        