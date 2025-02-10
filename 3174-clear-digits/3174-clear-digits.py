class Solution:
    def clearDigits(self, s: str) -> str:
        stk = ['']

        digits = '1234567890'
        alphabets = 'abcdefghijklmnop'

        for ch in s:
            if '0' <= ch <= '9' and 'a' <= stk[-1] <= 'z':
                stk.pop()
                continue
            else:
                stk.append(ch)
        return ''.join(stk)
