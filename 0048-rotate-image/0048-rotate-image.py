class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1. Transpose the matrix
        2. Reverse each row
        """

        self.transpose(matrix)
        for row in matrix:
            row.reverse()
        return
    
    def transpose(self, matrix: List[List[int]]) -> None:
        n_row = len(matrix)
        n_col = len(matrix[0])

        for r in range(n_row):
            for c in range(r+1, n_col):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return
        