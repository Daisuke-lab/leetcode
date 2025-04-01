class Solution:
    # Brute Force
    # DFS for all cells
    # Time Complexity is O(m*n)^2
    
    # you can cache the length memo[i][j] = length
    # 
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ROW = len(matrix)
        self.COL = len(matrix[0])
        self.matrix = matrix
        self.max_path = 1
        self.memo = [[-1 for j in range(self.COL)] for i in range(self.ROW)]
        for i in range(self.ROW):
            for j in range(self.COL):
                self.dfs(i, j)
        return self.max_path

    def dfs(self, i, j):
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        path = 1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for direction in directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or next_i == self.ROW or next_j < 0 or next_j == self.COL:
                continue
            if self.matrix[i][j] < self.matrix[next_i][next_j]:
                path = max(path, self.dfs(next_i, next_j)+1)
        self.memo[i][j] = path
        self.max_path = max(self.max_path, path)
        return path
        