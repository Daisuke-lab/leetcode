class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # If you find "0", just do dfs
        # dfs's output should be True or False
        # if the child is true, change yourself true
        # otherwise, add (i, j) in visited:
        # visited doesn't have to removed after propagation, it doesn't change the consequence
        # if (i, j) is edge return false
        # if (i, j) is surrounded by X or visited, return True
        # if you find one position that is Open, which means you find the escape
        # you want to flip finally. how can you keep track of positions
        # you also want to know open list that is already explored but it turns out open
        self.visited = set()
        self.explored = set()
        self.ROW = len(board)
        self.COL = len(board[0])
        self.board = board
        for i in range(self.ROW):
            for j in range(self.COL):
                if (i, j) not in self.visited and self.board[i][j] == "O":
                    self.positions = set()
                    result = self.dfs(i, j)
                    if result:
                        for x_i, x_j in self.positions:
                            self.board[x_i][x_j] = "X"
                    # else:
                    #     for x_i, x_j in positions:
                    #         self.explored((x_i, x_j))
        

    def dfs(self, i, j):
        self.visited.add((i, j))
        self.positions.add((i, j))
        if i == 0 or j == 0 or i == self.ROW - 1 or j == self.COL - 1:
            conqured = False
        else:
            conqured = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i < 0 or new_j < 0 or new_i == self.ROW or new_j == self.COL:
                continue
            if (new_i, new_j) not in self.visited and self.board[new_i][new_j] == "O":
                conqured = self.dfs(new_i, new_j) and conqured
        return conqured
        

                            