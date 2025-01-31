class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        def dfs(r: int, c: int, island: set[tuple[int, int]]):
            for i,j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nr = r+i
                nc = c+j
                if not (0 <= nr < nrow and 0 <= nc < ncol):
                    continue
                if grid[nr][nc] != 1:
                    continue
                if (nr, nc) in island:
                    continue
                grid[nr][nc] = -1
                island.add( (nr, nc) )
                dfs(nr, nc, island)
            return island

        size = {}
        islands = []
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] != 1:
                    continue
                islands.append(dfs(r, c, { (r, c) }))

                key = object()
                for i, j in islands[-1]:
                    grid[i][j] = key
                size[key] = len(islands[-1])
        
        def get(r: int, c: int):
            area = 1
            indices = set()
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nr, nc = r+i, c+j
                if not (0 <= nr < nrow and 0 <= nc < ncol):
                    continue
                id = grid[nr][nc]
                indices.add(id)
                
            for id in indices:
                area += size.get(id, 0)

            return area

        answer =  max( map(len, islands) ) if islands else 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] != 0:
                    continue
                answer = max( answer, get(r, c) )
        return answer

        
