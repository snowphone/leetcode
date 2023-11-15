from itertools import chain
from collections import defaultdict
from heapq import heappush, heappop

from queue import SimpleQueue

class PQ(list):
    def put(self, it):
        heappush(self, it)
    def get(self):
        return heappop(self)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n_line = len(routes)
        lines = defaultdict(list)  # bus stop to available line

        for line, route in enumerate(routes):
            for busstop in route:
                lines[busstop].append(line)

        for i in range(len(routes)):
            routes[i] = set(routes[i])
        

        source_lines = set(i for i in range(n_line) if source in routes[i])
        target_lines = set(i for i in range(n_line) if target in routes[i])

        graph = defaultdict(set)
        for i in range(n_line):
            graph[i] = {
                it
                for bus in routes[i]
                for it in lines[bus]
                if it != i
            }


        q = SimpleQueue()
        visited = set()
        for source_line in source_lines:
            q.put( (1, source_line) )
            visited.add(source_line)

        while not q.empty():
            acc_cost, me = q.get(block=False)

            if me in target_lines:
                return acc_cost

            for adj in graph[me]:
                if adj in visited:
                    continue
                visited |= {adj}
                q.put( (acc_cost + 1, adj) )
        return -1

