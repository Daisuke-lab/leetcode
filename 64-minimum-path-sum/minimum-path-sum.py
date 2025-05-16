class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        memo = [[
            grid[i][j] for j in range(COL)]
            for i in range(ROW)]
        for i in range(ROW -1, -1, -1):
            for j in range(COL -1, -1, -1):
                if i == ROW -1 and j == COL -1:
                    memo[i][j] = grid[i][j]
                elif i == ROW - 1:
                    memo[i][j] += memo[i][j+1]
                elif j == COL - 1:
                    memo[i][j] += memo[i+1][j]
                else:
                    memo[i][j] += min(memo[i+1][j], memo[i][j+1])
        return memo[0][0]
        