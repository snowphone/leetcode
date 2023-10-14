from functools import cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def fn(idx: int, remaining_walls: int):
            if remaining_walls <= 0:
                return 0
            if idx == n:
                return float('inf')
            
            return min(
                fn(idx + 1, remaining_walls),  # Don't paint
                cost[idx] + fn(idx + 1, remaining_walls - (1 + time[idx])),  # Don't paint
            )
            
        return fn(0, n)