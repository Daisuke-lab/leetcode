class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        
        grid = [[0 for j in range(COL)] for i in range(ROW)]
        max_length = 0
        for i in range(ROW):
            for j in range(COL):
                if i == 0 or j == 0:
                    grid[i][j] = int(matrix[i][j])
                    max_length = max(max_length, grid[i][j])
                    continue
                if matrix[i][j] == '1':
                    ensured_length = min(grid[i-1][j], grid[i][j-1])
                    possible_length = ensured_length + 1
                    dig_i = i - (possible_length - 1)
                    dig_j = j - (possible_length - 1)
                    if matrix[dig_i][dig_j] == "1":
                        grid[i][j] = possible_length
                    elif ensured_length > 0:
                        grid[i][j] = ensured_length
                    else:
                        grid[i][j] = 1
                    max_length = max(max_length, grid[i][j])
        return max_length**2