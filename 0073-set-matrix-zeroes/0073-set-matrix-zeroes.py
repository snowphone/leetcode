class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_row = len(matrix)
        n_col = len(matrix[0])
        def clear(r, c):
            for i in range(n_row):
                matrix[i][c] = 0
            for j in range(n_col):
                matrix[r][j] = 0
        

        tmp = []
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] != 0:
                    continue
                tmp.append( (i, j) )
        for i, j in tmp:
            clear(i, j)