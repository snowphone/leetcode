class Solution:
    @staticmethod
    def typed(s: str):
        stk = []
        for ch in s:
            if ch != '#':
                stk.append(ch)
                continue
            
            if not stk:
                continue
            stk.pop()
        return ''.join(stk)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.typed(s) == self.typed(t)
