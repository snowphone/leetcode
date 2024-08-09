class Solution:
    def _is_magic_square(self, upper_left: tuple[int, int], grid):
        r, c = upper_left

        elements = sorted(grid[r][c:c+3]+grid[r+1][c:c+3]+ grid[r+2][c:c+3])

        if elements != list(range(1,10)):
            return False

        sums = {
            sum(grid[r][c:c+3]),
            sum(grid[r+1][c:c+3]),
            sum(grid[r+2][c:c+3]),
            grid[r][c] + grid[r+1][c] + grid[r+2][c],
            grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1],
            grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2],
            grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2],
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c],
        }

        return len(sums) == 1

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        answer = 0
        for r in range(nrow):
            if r+2 >= nrow:
                continue
            for c in range(ncol):
                if c+2 >= ncol:
                    continue

                upper_left = (r, c)
                if self._is_magic_square(upper_left, grid):
                    answer += 1
        return answer