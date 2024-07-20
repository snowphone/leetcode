class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        nrow = len(rowSum)
        ncol = len(colSum)

        matrix = [
            [rowSum[r]] + [0] * (ncol-1)
            for r in range(nrow)
        ]

        for c in range(ncol - 1):
            acc = sum(matrix[i][c] for i in range(nrow))
            i = 0
            while acc > colSum[c]:
                diff = acc - colSum[c]
                to_move = min(matrix[i][c], diff)
                matrix[i][c] -= to_move
                matrix[i][c+1] += to_move
                acc -= to_move
                i += 1 

        return matrix