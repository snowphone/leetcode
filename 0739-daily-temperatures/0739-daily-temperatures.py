class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = [(0, temperatures[0])]
        answer = [0 for _ in range(n)]
        for i in range(1, n):
            it = temperatures[i]
            while stk and stk[-1][1] < it:
                j, jt = stk[-1]
                stk.pop()
                answer[j] = i - j

            stk.append( (i, it) )
        
        return answer