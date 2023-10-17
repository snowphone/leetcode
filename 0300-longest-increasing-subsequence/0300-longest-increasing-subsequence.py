from sortedcontainers import SortedSet
from operator import itemgetter
from heapq import heappush, heappop

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def fn(idx):
            if idx == 0:
                return 1
            
            answer = 0
            it = nums[idx]
            for i in range(idx):
                jt = nums[i]
                if jt >= it:
                    continue
                answer = max(answer, fn(i))
            return answer + 1
        
        return max(fn(i) for i in range(len(nums)))
