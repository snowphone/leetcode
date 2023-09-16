class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [(0, temperatures[0])]
        answer = [0 for _ in temperatures]
        for i, it in enumerate(temperatures[1:], 1):
            while stk and stk[-1][1] < it:
                j, jt = stk[-1]
                stk.pop()
                answer[j] = i - j

            stk.append( (i, it) )
        
        return answer