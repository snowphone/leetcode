class Solution:
    def transpose(self, matrix):
        n_row = len(matrix)
        n_col = len(matrix[0])

        for i in range(n_row):
            for j in range(i+1, n_col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

    def rev(self, matrix):
        for line in matrix:
            line.reverse()
        return

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.rev(matrix)
        return