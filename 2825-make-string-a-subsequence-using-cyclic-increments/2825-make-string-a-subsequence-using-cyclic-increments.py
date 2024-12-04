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
    
    def _dec(self, s: str):
        chars = [chr(ord(it) - 1) if it != 'a' else 'z' for it in s]
        return ''.join(chars)

    def _sim(self, lhs, rhs):
        return lhs in [rhs, self._dec(rhs)]
        