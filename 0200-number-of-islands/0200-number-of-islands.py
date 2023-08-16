class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = '0'
        LAND = '1'
        
        n_row = len(grid)
        n_col = len(grid[0])

        def dfs(r, c):
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = r + i
                new_c = c + j
                if not (0 <= new_r < n_row):
                    continue
                if not (0 <= new_c < n_col):
                    continue
                if grid[new_r][new_c] != LAND:
                    continue
                
                grid[new_r][new_c] = WATER
                dfs(new_r, new_c)
            return
        

        answer = 0
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == WATER:
                    continue
                answer += 1
                dfs(r, c)
        return answer