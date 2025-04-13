class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        
        grid = [[0 for j in range(COL+1)] for i in range(ROW + 1)]
        max_length = 0
        for i in range(1, ROW + 1):
            for j in range(1, COL + 1):
                if matrix[i-1][j-1] == '1':
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1]) + 1
                    max_length = max(max_length, grid[i][j])
        return max_length**2