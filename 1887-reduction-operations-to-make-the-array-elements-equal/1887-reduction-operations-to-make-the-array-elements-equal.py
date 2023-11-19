from collections import Counter
from itertools import groupby

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()

        grouped = [
            (it, len( list(j)) )
            for it, j in groupby(nums, key=lambda i: i)
        ]
        answer = 0
        for i, (it, cnt) in enumerate(grouped):
            answer += (i * cnt)

        return answer
            