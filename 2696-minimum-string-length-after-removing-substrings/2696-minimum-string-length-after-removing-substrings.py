class Solution:
    def minLength(self, s: str) -> int:
        stk = []

        for ch in s:
            if stk and (stk[-1], ch) in [('A', 'B'), ('C', 'D')]:
                stk.pop()
                continue
            stk.append(ch)
        return len(stk)