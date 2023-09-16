from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 987654321
        graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
        for f, t, e in times:
            graph[f][t] = e
        
        q = PriorityQueue()
        q.put( (0, k) )  # Accumulated latency, node

        remaining = set(range(1, n+1))
        while remaining:
            latency, it = q.get()
            if it not in remaining:
                continue
            remaining -= {it}

            if not remaining and latency != INF:
                return latency

            for jt in range(1, n+1):
                if it == jt:
                    continue
                edge = graph[it][jt]
                q.put( (latency + edge, jt) )

        return -1
