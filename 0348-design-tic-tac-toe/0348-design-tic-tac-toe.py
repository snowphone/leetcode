class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [ [None for _ in range(n)] for _ in range(n) ]
        return
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self._make_it(row, col, player):
            return player
        return 0

    
    def _make_it(self, row: int, col: int, player: int):
        n = self.n
        return (
            all(self.board[row][j] == player for j in range(n)) or  # -
            all(self.board[i][col] == player for i in range(n)) or  # |
            all(self.board[i][i] == player for i in range(n))   or  # \
            all(self.board[i][n-i-1] == player for i in range(n))   # /
        )
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)