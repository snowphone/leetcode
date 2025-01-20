from sortedcontainers import SortedList


class PQ:
    "Sorted in ascending order"
    def __init__(self):
        self.q = SortedList()

    def put(self, item):
        return self.q.add(item)

    def get(self):
        return self.q.pop(0)

    def __bool__(self):
        return bool(self.q)


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        delta_q = PQ()
        for idx in count(0):
            if idx == len(heights) - 1:
                return idx
            current, nxt = heights[idx : idx + 2]
            if current >= nxt:
                continue
            delta_q.put(nxt - current)
            if ladders:
                ladders -= 1
            elif delta_q and (delta := delta_q.get()) <= bricks:
                bricks -= delta  # Replace a ladder with bricks
            else:
                break
        return idx
