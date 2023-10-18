class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_row = len(matrix)
        n_col = len(matrix[0])

        row_flag = [False] * n_row
        col_flag = [False] * n_col

        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] != 0:
                    continue
                row_flag[r] = True
                col_flag[c] = True
        
        for r in range(n_row):
            if not row_flag[r]:
                continue
            for c in range(n_col):
                matrix[r][c] = 0

        for c in range(n_col):
            if not col_flag[c]:
                continue
            for r in range(n_row):
                matrix[r][c] = 0
        return
