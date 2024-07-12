class Solution:
    @cache
    def maximumGain(self, s: str, x: int, y: int) -> int:
        sz = len(s)
        answer = 0
        for i in range(sz-1):
            if s[i:i+2] == 'ab':
                answer = max(answer, x + self.maximumGain(s[:i] + s[i+2:], x, y) )
            if s[i:i+2] == 'ba':
                answer = max(answer, y + self.maximumGain(s[:i] + s[i+2:], x, y) )
        return answer