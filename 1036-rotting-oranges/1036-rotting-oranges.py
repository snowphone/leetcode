from queue import SimpleQueue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col =len(grid[0])

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        q = SimpleQueue()
        n_fresh = 0
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == FRESH:
                    n_fresh += 1
                    continue
                if grid[r][c] == ROTTEN:
                    q.put( (r, c, 0) )
                    continue
        
        if not n_fresh:
            return 0

        while not q.empty():
            r, c, minute = q.get()

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + i
                nc = c + j
                if not (0 <= nr < n_row):
                    continue
                if not (0 <= nc < n_col):
                    continue
                if grid[nr][nc] != FRESH:
                    continue
                    
                grid[nr][nc] = ROTTEN
                n_fresh -= 1
                if not n_fresh:
                    return minute + 1

                q.put( (nr, nc, minute + 1) )
        
        return -1 if n_fresh else 0
                
                
