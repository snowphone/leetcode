class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_row = len(matrix)
        n_col = len(matrix[0])

        def row_fill(r):
            for c in range(n_col):
                if matrix[r][c] == 0:
                    continue
                matrix[r][c] = None
        def col_fill(c):
            for r in range(n_row):
                if matrix[r][c] == 0:
                    continue
                matrix[r][c] = None

        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] != 0:
                    continue
                row_fill(r)
                col_fill(c)

        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] is not None:
                    continue
                matrix[r][c] = 0
        return
