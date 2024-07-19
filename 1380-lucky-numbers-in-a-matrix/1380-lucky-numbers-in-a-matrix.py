class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        nrow = len(matrix)
        ncol = len(matrix[0])

        max_on_columns = set(
            (max(range(nrow), key=lambda i: matrix[i][j]), j) for j in range(ncol)
        )
        min_on_rows = set(
            (i, min(range(ncol), key=lambda j: matrix[i][j])) for i in range(nrow)
        )

        return [
            matrix[i][j] for i, j in (max_on_columns & min_on_rows)
        ]