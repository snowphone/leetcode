from heapq import heappush, heappop

class HQ:
    def __init__(self, fn):
        self.q = []
        self.fn = fn
        return
    
    def put(self, item):
        heappush(self.q, (self.fn(item), item))

    def get(self):
        return heappop(self.q)[1]

class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False for _ in nums]
        q = HQ(lambda it: it)
        for i, it in enumerate(nums):
            q.put((it, i))
        remaining = set(range(len(nums)))

        score = 0
        while remaining:
            it, i = q.get()
            if i not in remaining:
                continue
            score += it
            remaining -= {i-1, i, i+1}
        return score