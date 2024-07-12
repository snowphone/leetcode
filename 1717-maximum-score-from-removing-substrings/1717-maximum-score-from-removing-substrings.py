class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            pattern1, point1 = 'ab', x
            pattern2, point2 = 'ba', y
        else:
            pattern1, point1 = 'ba', y
            pattern2, point2 = 'ab', x

        stk = ['']
        answer = 0
        for ch in s:
            if stk[-1] + ch == pattern1:
                answer += point1
                stk.pop()
            else:
                stk.append(ch)
        
        stk, s = [''], ''.join(stk)
        for ch in s:
            if stk[-1] + ch == pattern2:
                answer += point2
                stk.pop()
            else:
                stk.append(ch)
                
        return answer