from collections import Counter
from heapq import heappush, heappop

class Heap(list):
    def __init__(self, key):
        super().__init__(self)
        self.key = key
    
    def put(self, item):
        heappush(self, (self.key(item), item) )
    
    def get(self):
        return heappop(self)[1]

    def peak(self):
        return self[0][1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = Heap(key=lambda it: counter[n] )  # Pop the fewest first
        for n in counter.keys():
            heap.put(n)
            while len(heap) > k:
                heap.get()
        
        answer = []
        while heap:
            answer.append(heap.get())
        return answer