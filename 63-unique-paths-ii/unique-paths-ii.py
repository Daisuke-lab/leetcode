class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        ROW = len(grid)
        COL = len(grid[0])
        memo = [[
            -1 for j in range(COL)]
            for i in range(ROW)]
        for i in range(ROW -1, -1, -1):
            for j in range(COL -1, -1, -1):
                if grid[i][j] == 1:
                    memo[i][j] = 0
                elif j == COL -1 and i == ROW - 1:
                    memo[i][j] = 1
                elif j == COL -1:
                    memo[i][j] = memo[i+1][j]
                elif i == ROW - 1:
                    memo[i][j] = memo[i][j +1]
                else:
                    memo[i][j] = memo[i+1][j] + memo[i][j +1]
            
        return memo[0][0]
        