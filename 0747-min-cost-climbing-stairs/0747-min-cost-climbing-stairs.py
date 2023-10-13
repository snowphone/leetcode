from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climb(idx: int):
            if idx <= 1:
                return 0
            return min(cost[idx-1] + climb(idx-1) , cost[idx-2] + climb(idx-2) )

        return climb( len(cost) )