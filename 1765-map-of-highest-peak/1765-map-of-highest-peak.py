from queue import SimpleQueue
from typing import Annotated

# row, col, current height
Entry = Annotated[tuple[int, int, int], ...]


class Solution:

    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        UNUSED = -1
        nrow = len(isWater)
        ncol = len(isWater[0])
        matrix = [[UNUSED for _ in range(ncol)] for _ in range(nrow)]

        q = SimpleQueue[Entry]()

        for r in range(nrow):
            for c in range(ncol):
                if isWater[r][c]:
                    matrix[r][c] = 0
                    q.put((r, c, 0))

        def get_adjacents(r: int, c: int):
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                adj_r = r + i
                adj_c = c + j
                if (
                    not (0 <= adj_r < nrow) or
                    not (0 <= adj_c < ncol) or
                    isWater[adj_r][adj_c] or
                    matrix[adj_r][adj_c] != UNUSED
                ):
                    continue
                yield (adj_r, adj_c)

        while not q.empty():
            r, c, h = q.get()

            for adj_r, adj_c in get_adjacents(r, c):
                new_h = h + 1
                matrix[adj_r][adj_c] = new_h
                q.put((adj_r, adj_c, new_h))

        return matrix
