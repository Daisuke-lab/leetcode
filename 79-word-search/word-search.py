class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # looks like dfs
        # can you use DP? well technical you can. but it can be tricky because it's 4 directions
        # you can make subproblem with word, but maybe not with board

        # 1. first starting poitn
        # 2. dig
        # Time complexity is O(2m*n) one for finding starting point and, second to dig

        self.board = board
        self.word = word
        self.ROW = len(self.board)
        self.COL = len(self.board[0])
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.board[i][j] == self.word[0]:
                    visited = set()
                    result = self.dig(i, j, self.word, visited)
                    if result:
                        return True
        return False

    def dig(self, i, j, word, visited):
        if word == "":
            return True
        if i < 0 or i == self.ROW or j < 0 or j == self.COL:
            return False
        if (i, j) in visited:
            return False
        
        if self.board[i][j] == word[0]:
            visited.add((i, j))
            result = self.dig(i-1, j, word[1:], visited.copy())
            result = self.dig(i+1, j, word[1:], visited.copy()) or result
            result = self.dig(i, j-1, word[1:], visited.copy()) or result
            result = self.dig(i, j+1, word[1:], visited.copy()) or result
            return result
        else:
            return False