class Solution:
    # DFS from the edges
    # change O to P
    # after that, go through matrix, changing O to X and P to O
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROW = len(board)
        self.COL = len(board[0])
        self.board = board
        for i in range(self.ROW):
            self.mark_safe_zone(i, 0)
            self.mark_safe_zone(i, self.COL - 1)
        for j in range(self.COL):
            self.mark_safe_zone(0, j)
            self.mark_safe_zone(self.ROW - 1, j)
        for i in range(self.ROW):
            for j in range(self.COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"
        


    def mark_safe_zone(self, i, j):
        if i < 0 or j < 0 or i >= self.ROW or j >= self.COL:
            return 
        elif self.board[i][j] in ["X", "P"]:
            return
        self.board[i][j] = "P"
        self.mark_safe_zone(i-1, j)
        self.mark_safe_zone(i+1, j)
        self.mark_safe_zone(i, j-1)
        self.mark_safe_zone(i, j+1)

        