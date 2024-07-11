class Solution:
    def reverseParentheses(self, s: str) -> str:
        sz = len(s)
        stk = []

        for ch in s:
            stk.append(ch)

            if ch != ')':
                continue
            sz = len(stk)
            i = next(i for i in range(sz-1, -1, -1) if stk[i] == '(')    
            chunk = stk[i+1:-1]  # parentheses not included
            stk = stk[:i] + chunk[::-1]

        return ''.join(stk)