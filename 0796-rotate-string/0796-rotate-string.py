class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        return any(
            self._shift(s, i) == goal for i in range(n+1)
        )
    
    def _shift(self, s: str, n: int):
        return s[n:] + s[:n]