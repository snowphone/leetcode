class Solution:
    def reverseParentheses(self, s: str) -> str:
        portal = dict()

        # Discover and create a portal
        stk = []
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            elif ch == ')':
                j = stk.pop()
                portal[i] = j
                portal[j] = i
        
        idx, step = 0, 1

        answer = []
        for _ in s:
            if idx in portal:
                idx = portal[idx]
                step *= -1
            else:
                answer.append(s[idx])
            
            idx += step
        return ''.join(answer)
                