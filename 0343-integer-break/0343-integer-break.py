from functools import reduce
from operator import mul

class Solution:
    def integerBreak(self, n: int) -> int:
        k = 2
        answer = 0
        while n // k:
            remainder =  n % k
            nums = [n // k for _ in range(k)]
            for i in range(remainder):
                nums[i] += 1
            
            answer = max(answer,  reduce(mul, nums) )
            
            k += 1
        return answer