class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        
        ch = s[0]
        if ch == '0':
            return 0
        if '3' <= ch <= '9':
            return self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])


