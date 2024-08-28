from queue import SimpleQueue

ISLAND = 1

GridType = List[List[int]]

class Solution:
    def countSubIslands(self, grid1: GridType, grid2: GridType) -> int:
        islands = self._get_subislands(grid1, grid2)

        return len(islands)

    def _get_subislands(self, main: GridType, sub: GridType):
        nrow=len(sub)
        ncol=len(sub[0])

        visited = set()

        islands = []
        for r in range(nrow):
            for c in range(ncol):
                if not (sub[r][c] == ISLAND and main[r][c] == ISLAND):
                    continue
                if (r, c) in visited:
                    continue
                island = self._scan(sub, main, r, c)
                if island is None:
                    continue
                islands.append(island)
                visited |= island

        return islands
    
    def _scan(self, grid: GridType, main: GridType, start_r: int, start_c: int) -> frozenset[tuple[int, int]]|None:
        nrow=len(grid)
        ncol=len(grid[0])

        bag = set()
        q = SimpleQueue()
        q.put((start_r, start_c))

        def not_overlapped(r: int, c: int):
            return grid[r][c] == ISLAND and main[r][c] != ISLAND

        while not q.empty():
            r, c = q.get()
            bag.add((r, c))
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newr = r + i
                newc = c + j
                if (
                    not (0 <= newr < nrow) or
                    not (0 <= newc < ncol)
                ):
                    continue
                if grid[newr][newc] != ISLAND:
                    continue
                if not_overlapped(newr, newc):
                    return None
                if (newr, newc) in bag:
                    continue
                q.put((newr, newc))

        return frozenset(bag)
        