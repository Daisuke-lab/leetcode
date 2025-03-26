class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.ROW = len(board)
        self.COL = len(board[0])
        for j in range(self.COL):
            first_row = 0
            last_row = self.ROW - 1
            if board[first_row][j] == "O":
                self.dfs(first_row, j)
            if board[last_row][j] == "O":
                self.dfs(last_row, j)
        
        for i in range(self.ROW):
            first_col = 0
            last_col = self.COL - 1
            if board[i][first_col] == "O":
                self.dfs(i, first_col)
            if board[i][last_col] == "O":
                self.dfs(i, last_col)

        for i in range(self.ROW):
            for j in range(self.COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O" 
    
    def dfs(self, i, j):
        if i < 0 or i == self.ROW or j < 0 or j == self.COL:
            return
        if self.board[i][j] != "O":
            return

        self.board[i][j] = "T"
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            self.dfs(new_i, new_j)

                            