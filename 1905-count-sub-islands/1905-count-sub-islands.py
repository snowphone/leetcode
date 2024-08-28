from queue import SimpleQueue

ISLAND = 1
VISITED = 2

GridType = List[List[int]]

class Solution:
    def countSubIslands(self, grid1: GridType, grid2: GridType) -> int:
        return self._get_subislands(grid1, grid2)

    def _get_subislands(self, main: GridType, sub: GridType):
        nrow=len(sub)
        ncol=len(sub[0])

        answer = 0
        for r in range(nrow):
            for c in range(ncol):
                if not (sub[r][c] == ISLAND and main[r][c] == ISLAND):
                    continue
                ok = self._scan(sub, main, r, c)
                answer += int(ok)

        return answer
    
    def _scan(self, grid: GridType, main: GridType, start_r: int, start_c: int) -> bool:
        nrow=len(grid)
        ncol=len(grid[0])

        answer = True

        q = SimpleQueue()
        q.put((start_r, start_c))
        grid[start_r][start_c] = VISITED

        def only_on_main_island(r: int, c: int):
            return grid[r][c] == ISLAND and main[r][c] != ISLAND

        while not q.empty():
            r, c = q.get()

            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newr = r + i
                newc = c + j
                if (
                    not (0 <= newr < nrow) or
                    not (0 <= newc < ncol) or
                    grid[newr][newc] != ISLAND 
                ):
                    continue
                if only_on_main_island(newr, newc):
                    answer = False
                q.put((newr, newc))
                grid[newr][newc] = VISITED

        return answer
        