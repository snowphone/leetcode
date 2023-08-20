from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = PriorityQueue()

        for i in range(n - 1):
            height = heights[i+1] - heights[i]
            if height <= 0:
                continue
            q.put(height)
            if q.qsize() > ladders:
                bricks -= q.get()
            if bricks < 0:
                return i
                
        return n - 1