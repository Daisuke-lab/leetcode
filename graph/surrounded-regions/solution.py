from collections import deque
#1. 端でになっているのを#に変える。
#2. #に接しているOをwhile loopで#に変えていく。
#3. #にしたやつをOに戻して、#になっていないOはXに変える。


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.col_num = len(board)
        self.row_num = len(board[0])

        queue = deque()


        for i in range(self.col_num):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][self.row_num - 1] == "O":
                queue.append((i, self.row_num -1))

        for j in range(self.row_num):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[self.col_num-1][j] == "O":
                queue.append((self.col_num-1, j))

        while queue:
            i, j = queue.popleft()
            board[i][j] = "#"
            
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not self.inBounds(ii, jj):
                    continue
                if board[ii][jj] != "O":
                    continue
                
                queue.append((ii, jj))
                board[ii][jj] = "#"


        for i in range(self.col_num):
            for j in range(self.row_num):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"


    def inBounds(self, i,j):
        return (0 <= i < self.col_num) and (0 <= j < self.row_num)

    
