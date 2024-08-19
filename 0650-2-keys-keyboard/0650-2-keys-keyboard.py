class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2
        

        answer = n
        for i in range(2, n):
            if n % i != 0:
                continue
            
            answer = min(
                self.minSteps(n // i) + i,
                answer,
            )
        return answer

