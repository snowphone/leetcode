from sortedcontainers import SortedList

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.q = SortedList()
        self.k = k
        for it in nums:
            self.q.add(it)

            while len(self.q) > k:
                self.q.pop(0)

    def add(self, val: int) -> int:
        self.q.add(val)
        while len(self.q) > self.k:
            self.q.pop(0)
        return self.q[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)