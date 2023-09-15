from queue import PriorityQueue
from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(lhs, rhs):
            return abs(lhs[0] - rhs[0]) + abs(lhs[1] - rhs[1])

        points = [tuple(it) for it in points]
        
        it = points[0]
        used = { it }
        q = PriorityQueue()
        for jt in points:
            if it == jt:
                continue
            q.put( (manhattan(it, jt), jt) )

        answer = 0
        n = len(points)
        while len(used) < n:
            cost, it = q.get()
            if it in used:
                continue

            answer += cost
            used.add(it)


            for jt in points:
                if it == jt:
                    continue
                q.put( (manhattan(it, jt), jt) )

        return answer
        