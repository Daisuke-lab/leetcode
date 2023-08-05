class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.col_num = len(board)
        self.row_num = len(board[0])


        for i in range(1, self.col_num-1):
            for j in range(1, self.row_num-1):
                print(i, j)
                print(self.dig((i, j)))
                if board[i][j] == "O" and self.dig((i, j)):
                    self.flip(i, j)

    
    def flip(self, i, j):
        self.board[i][j] = "X"

    def dig(self, start):
        i, j = start
        while j > 0:
            j -= 1
            if self.board[i][j] == "X":
                break
            if j == 0: return False

        i, j = start
        while j < self.row_num -1:
            j += 1
            if self.board[i][j] == "X":
                break
            if j == self.row_num: return False

        i, j = start
        while i > 0:
            i -= 1
            if self.board[i][j] == "X":
                break
            if i == 0: return False

        i, j = start
        while i < self.col_num -1:
            i += 1
            if self.board[i][j] == "X":
                break
            if i == self.col_num: return False

        return True

