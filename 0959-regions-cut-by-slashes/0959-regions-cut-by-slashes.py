SPACE = 0
WALL = 1
VISITED = 2

class Solution:
    def _convert_to_dots(self, grid):
        n = len(grid)
        dots = [[None for _ in range(n * 2)] for _ in range(n * 2)]

        for i in range(n):
            for j in range(n):
                ch = grid[i][j]
                if ch == ' ':
                    dots[2*i][2*j] = SPACE; dots[2*i][2*j + 1] = SPACE
                    dots[2*i+1][2*j] = SPACE; dots[2*i+1][2*j + 1] = SPACE
                elif ch == '/':
                    dots[2*i][2*j] = SPACE; dots[2*i][2*j + 1] = WALL
                    dots[2*i+1][2*j] = WALL; dots[2*i+1][2*j + 1] = SPACE
                elif ch == '\\':
                    dots[2*i][2*j] = WALL; dots[2*i][2*j + 1] = SPACE
                    dots[2*i+1][2*j] = SPACE; dots[2*i+1][2*j + 1] = WALL
        return dots
    
    def _dfs(self, dots, r, c):
        n = len(dots)
        dots[r][c] = VISITED

        for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            newr = r + i
            newc = c + j
            if not (0 <= newr < n and 0 <= newc < n):
                continue
            if dots[newr][newc] != SPACE:
                continue
            self._dfs(dots, newr, newc)
        return

    def regionsBySlashes(self, grid: List[str]) -> int:
        dots = self._convert_to_dots(grid)
        answer = 0

        for r, line in enumerate(dots):
            for c, dot in enumerate(line):
                if dot != SPACE:
                    continue
                self._dfs(dots, r, c)
                answer += 1
        return answer
        