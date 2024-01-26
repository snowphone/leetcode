class Solution:
    def findPaths(self, n_row: int, n_col: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def fn(r: int, c: int, max_move: int):
            if not (0 <= r < n_row) or not (0 <= c < n_col):
                return 1
            if max_move == 0:
                return 0
            answer = 0
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                answer += fn(r+i, c+j, max_move - 1) % MOD
            return answer % MOD

        return fn(startRow, startColumn, maxMove)