from heapq import heappush, heappop, heapify
class HQ:
    def __init__(self, iter, fn):
        self.fn = fn
        self.q = [( self.fn(item), item) for item in iter]
        heapify(self.q)

    def put(self, item):
        heappush(self.q, (self.fn(item), item))

    def get(self):
        return heappop(self.q)[1]

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        answer = nums[:]
        key = lambda pair: [pair[1], pair[0]]
        q = HQ(enumerate(nums), key)

        for _ in range(k):
            i, it = q.get()
            answer[i] = it * multiplier
            q.put( (i, answer[i]) )

        return answer
