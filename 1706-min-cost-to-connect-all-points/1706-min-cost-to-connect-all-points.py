from queue import PriorityQueue
from heapq import heappush, heappop
from operator import itemgetter

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(lhs, rhs):
            return abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1])

        # remaining, cost
        remaining = { tuple(it): float('inf') for it in points }
        
        it = next(iter(remaining))
        remaining.pop(it)

        for k, v in remaining.items():
            remaining[k] = min(v, manhattan(it, k))

        answer = 0
        while remaining:
            it, cost = min(remaining.items(), key=itemgetter(1))
            answer += cost

            remaining.pop(it)
            for k, v in remaining.items():
                remaining[k] = min(v, manhattan(it, k))

        return answer
        