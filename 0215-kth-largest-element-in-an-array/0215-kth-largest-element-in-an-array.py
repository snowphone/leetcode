from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        K = len(nums) - k + 1
        for n in nums:
            heappush(heap, -n)
            if len(heap) > K:
                heappop(heap)
        
        return -heappop(heap)
        
