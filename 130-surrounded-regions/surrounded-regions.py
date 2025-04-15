class Solution:

    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.ROW = len(board)
        self.COL = len(board[0])
        self.check_safe_zone()
        self.conquer()
        return board

    def conquer(self):
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.board[i][j] == "O":
                    self.board[i][j] = "X"
                elif self.board[i][j] == "S":
                    self.board[i][j] = "O"
        
        
    def check_safe_zone(self):
        queue = collections.deque()
        for i in range(self.ROW):
            if self.board[i][0] == "O":
                queue.append((i, 0))
            if self.board[i][self.COL -1] == "O":
                queue.append((i, self.COL -1))
        for j in range(self.COL):
            if self.board[0][j] == "O":
                queue.append((0, j))
            if self.board[self.ROW-1][j] == "O":
                queue.append((self.ROW-1, j))
        while queue:
            i, j = queue.popleft()
            self.board[i][j] = "S"
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if next_i < 0 or next_j < 0 or next_i == self.ROW or next_j == self.COL:
                    continue
                if self.board[next_i][next_j] == "O":
                    queue.append((next_i, next_j))
                                    