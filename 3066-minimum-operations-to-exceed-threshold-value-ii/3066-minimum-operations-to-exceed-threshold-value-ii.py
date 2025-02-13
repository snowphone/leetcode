from heapq import heappop, heappush

class PQ(list):
    def put(self, item):
        heappush(self, item)
    def get(self):
        return heappop(self)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = PQ()
        smaller_than_k = 0
        for it in nums:
            q.put(it)
            if it < k:
                smaller_than_k += 1
        
        cnt = 0
        while smaller_than_k > 0 and len(q) > 1:
            x, y = q.get(), q.get()
            if x < k:
                smaller_than_k -= 1
            if y < k:
                smaller_than_k -= 1
            
            m, M = sorted([x, y])
            new_item = m * 2 + M
            if new_item < k:
                smaller_than_k += 1
            q.put(new_item)
            cnt += 1

        return cnt