from collections import Counter
from functools import cache

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(n):
            return int(str(n)[::-1])
        
        revCnt = Counter( [it - rev(it) for it in nums] )

        answer = 0
        for k, v in revCnt.items():
            if v == 1:
                continue
            answer += v * (v-1) // 2
        
        return answer % (10 ** 9 + 7)
                
                