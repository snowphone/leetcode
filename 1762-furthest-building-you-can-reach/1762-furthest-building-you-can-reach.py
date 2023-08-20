from heapq import heappush, heappop
class PQ(list):
    def __init__(self):
        super().__init__()
        return
    
    def put(self, item):
        heappush(self, item)

    def get(self):
        return heappop(self)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = PQ()

        for i in range(n - 1):
            height = heights[i+1] - heights[i]
            if height <= 0:
                continue
            q.put(height)
            if len(q) > ladders:
                bricks -= q.get()
            if bricks < 0:
                return i
                
        return n - 1