class Solution:
    def shortestPalindrome(self, s: str) -> str:
        sz = len(s)
        rev = s[::-1]

        return next(
            (
                rev[:i] + s
                for i in range(sz)
                if s[: sz - i] == rev[i:]
            ), ''
        )