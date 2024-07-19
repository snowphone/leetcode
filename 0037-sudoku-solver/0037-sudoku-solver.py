class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        remaining_cells = self._get_empty_cells(board)
        remaining_cells.sort(key=lambda it: (it[0]//3, it[1]//3))

        self._try(board, remaining_cells)
        return

    def _get_empty_cells(self, board):
        return [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]

    def _try(self, board, remaining_cells):
        if not remaining_cells:
            return True
        r, c = remaining_cells.pop()

        candidates = self._get_available_nums(board, r, c)
        for candidate_num in candidates:
            board[r][c] = str(candidate_num)
            if self._try(board, remaining_cells):
                return True

        board[r][c] = "."
        remaining_cells.append((r, c))
        return False

    def _get_group_upper_left(self, r, c):
        """
        Returns the most upper left cell of 3x3 sub-matrix
        """
        return (r // 3) * 3, (c // 3) * 3

    def _get_available_nums(self, board, r, c):
        start_r, start_c = self._get_group_upper_left(r, c)

        N = set(range(1, 10))
        submatrix_nums = set(
            int(board[i][j])
            for i in range(start_r, start_r + 3)
            for j in range(start_c, start_c + 3)
            if board[i][j] != "."
        )
        row_nums = set(int(board[r][j]) for j in range(9) if board[r][j] != ".")
        col_nums = set(int(board[i][c]) for i in range(9) if board[i][c] != ".")

        return (N - submatrix_nums) & (N - row_nums) & (N - col_nums)