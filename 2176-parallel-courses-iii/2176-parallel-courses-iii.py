from queue import SimpleQueue

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        "I think it requires to find the critical path"

        graph = defaultdict(list)
        indegree = [0 for _ in range(n) ]
        for f, t in relations:
            f -= 1
            t -= 1
            graph[f].append(t)
            indegree[t] += 1
        
        starts = [ i for i, cnt in enumerate(indegree) if cnt == 0 ]

        @cache
        def path_cost(idx: int):
            cost = 0

            for nxt in graph[idx]:
                cost = max(cost, path_cost(nxt))  # Most expensive, not longest actually

            return cost + time[idx]

        return max(path_cost(i) for i in starts)
