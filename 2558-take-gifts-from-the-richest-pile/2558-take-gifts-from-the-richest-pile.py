from heapq import heappop, heappush
from operator import neg

class HQ:
    def __init__(self, fn, iter):
        self.q = []
        self.fn = fn

        for it in iter:
            self.put(it)

    def put(self, item):
        heappush(self.q, (self.fn(item), item))
    
    def get(self):
        return heappop(self.q)[1]

    def __iter__(self):
        return (it[1] for it in self.q)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = HQ(neg, gifts)
        
        for _ in range(k):
            n = heap.get()
            heap.put( int(n ** 0.5) )

        return sum(heap)
