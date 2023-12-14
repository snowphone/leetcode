class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n_row = len(grid)
        n_col = len(grid[0])

        @cache
        def rowcnt(i):
            one = 0
            zero = 0
            for j in range(n_col):
                if grid[i][j] == 1:
                    one += 1
                else:
                    zero += 1
            return one - zero
        @cache
        def colcnt(j):
            one = 0
            zero = 0
            for i in range(n_row):
                if grid[i][j] == 1:
                    one += 1
                else:
                    zero += 1
            return one - zero
        
        return [
            [
                rowcnt(r) + colcnt(c)
                for c in range(n_col)
            ] for r in range(n_row)
        ]