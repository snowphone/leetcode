class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch in ['(', '[', '{']:
               stk.append(ch)
            elif stk and (stk[-1], ch) in [tuple('()'), tuple('[]'), tuple('{}')]:
                stk.pop()
            else:
                return False
        return not stk