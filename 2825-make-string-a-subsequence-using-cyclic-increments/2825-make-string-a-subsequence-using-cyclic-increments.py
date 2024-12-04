class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        r = 0
        for l, lit in enumerate(str1):
            if r == len(str2):
                break
            rit = str2[r]
            if self._sim(lit, rit):
                r += 1

        return r == len(str2)
    
    def _inc(self, ch: str):
        if ch == 'z':
            return 'a'
        return chr(ord(ch) + 1)

    def _sim(self, lhs, rhs):
        return rhs in [lhs, self._inc(lhs)]
        