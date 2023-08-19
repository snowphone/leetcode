from heapq import *
class Heap(list):
    def __init__(self, key: Callable):
        super().__init__()
        self.key = key
    
    def put(self, item):
        heappush(self, (self.key(item), item) )

    def get(self):
        return heappop(self)[1]

    def peak(self):
        return self[0][1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # /\
        heap = Heap(key=lambda it: it)
        for n in nums:
            heap.put(n)
            while len(heap) > k:
                heap.get()
        return heap.peak()