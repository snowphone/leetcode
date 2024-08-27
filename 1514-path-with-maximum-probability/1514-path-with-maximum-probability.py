from heapq import heappush, heappop
from math import log, e

class PQ(list):
    def __init__(self):
        super().__init__()
        return

    def put(self, nd, prob):
        heappush(self, (-prob, nd))
        return
    
    def get(self):
        prob, nd = heappop(self)
        return nd, -prob


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        INIT = 0
        adjs = defaultdict(list)

        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            adjs[a].append((b, prob))
            adjs[b].append((a, prob))
        
        distances = [0 for _ in range(n)]
        distances[start_node] = 1

        q = PQ()
        for nd, dist in enumerate(distances):
            q.put(nd, dist)

        while q:
            nd, pb = q.get()
            
            if nd == end_node:
                break
            
            for adj, p in adjs[nd]:
                new = distances[nd] * p
                if distances[adj] < new:
                    distances[adj] = new
                    q.put(adj, new)
        
        return distances[end_node]
        