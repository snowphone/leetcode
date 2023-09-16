from copy import copy, deepcopy
from operator import itemgetter
from queue import PriorityQueue, SimpleQueue

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n_row = len(heights)
        n_col = len(heights[0])

        # Graph-ize
        graph = defaultdict(lambda: defaultdict(int) )
        for r in range(n_row):
            for c in range(n_col):
                it = (r, c)
                h1 = heights[r][c]

                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+i, c+j
                    if not (0 <= nr < n_row):
                        continue
                    if not (0 <= nc < n_col):
                        continue
                    # Adjacent
                    h2 = heights[nr][nc]
                    jt = (nr, nc)
                    graph[it][jt] = abs(h1-h2)
                    graph[jt][it] = abs(h1-h2)

        # Dijkstra
        remaining = set(graph.keys())
        q = PriorityQueue()
        for it in graph.keys():
            q.put( (987654321, it) )
        q.put( (0, (0, 0) ) )

        while remaining:
            acc_cost, it = q.get()
            if it not in remaining:
                continue
            remaining.remove(it)

            if it == (n_row - 1, n_col - 1):
                return acc_cost

            for adj in graph[it].keys():
                edge = graph[it][adj]
                new_cost = max(acc_cost , edge)
                q.put( (new_cost, adj) )
        return 0








