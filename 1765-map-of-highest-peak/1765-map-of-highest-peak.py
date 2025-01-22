from queue import SimpleQueue
from typing import Annotated

# row, col, current height
Entry = Annotated[tuple[int, int, int], ...]

UNUSED = -1


class Solution:

    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        nrow = len(isWater)
        ncol = len(isWater[0])
        matrix = [[UNUSED for _ in range(ncol)] for _ in range(nrow)]

        qset = set[Entry]()
        q = SimpleQueue[Entry]()

        def put(item: Entry):
            if item in qset:
                return
            qset.add(item)
            q.put(item)
            return

        def get():
            item = q.get()
            qset.remove(item)
            return item

        for r in range(nrow):
            for c in range(ncol):
                if isWater[r][c]:
                    matrix[r][c] = 0
                    put((r, c, 0))

        def get_adjacents(r: int, c: int):
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                adj_r = r + i
                adj_c = c + j
                if not (0 <= adj_r < nrow):
                    continue
                if not (0 <= adj_c < ncol):
                    continue
                if isWater[adj_r][adj_c]:
                    continue
                if matrix[adj_r][adj_c] != UNUSED:
                    continue
                yield (adj_r, adj_c)

        while not q.empty():
            r, c, h = get()

            for adj_r, adj_c in get_adjacents(r, c):
                new_h = h + 1
                matrix[adj_r][adj_c] = new_h
                put((adj_r, adj_c, new_h))

        return matrix