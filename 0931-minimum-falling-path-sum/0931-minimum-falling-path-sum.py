class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])

        @cache
        def fn(r, c):
            if not (0 <= r < n_row):
                return 987654321
            if not (0 <= c < n_col):
                return 987654321
            
            if r + 1 == n_row:
                return matrix[r][c]
            

            return matrix[r][c] + min(
                fn(r+1, c+i) for i in [-1, 0, 1]
            )
        
        return min(
            fn(0, j) for j in range(n_col)
        )