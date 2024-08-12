from heapq import heappush, heappop

class PQ(list):
    def __init__(self):
        super().__init__()
        return
    def put(self, item):
        return heappush(self, item)
    def get(self):
        return heappop(self)
    def peek(self):
        return self[0]

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.q = PQ()
        self.k = k
        for it in nums:
            self.q.put(it)

            while len(self.q) > k:
                self.q.get()

    def add(self, val: int) -> int:
        self.q.put(val)
        while len(self.q) > self.k:
            self.q.get()
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)