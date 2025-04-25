class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        largest_square = 1
        self.grid = grid
        ROW = len(grid)
        COL = len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                k = 1
                row_sum = grid[i][j]
                col_sum = grid[i][j]
                while i + k < ROW and j + k < COL:
                    row_sum += grid[i+k][j]
                    col_sum += grid[i][j+k]
                    if row_sum == col_sum and k + 1 > largest_square and self.is_magic_square(i, j, k + 1, row_sum):
                        largest_square = k + 1
                    k += 1
        return largest_square
    
    def is_magic_square(self, i, j, length, target_sum):
        for p in range(length):
            if sum([self.grid[i+p][j+q] for q in range(length)]) != target_sum:
                return False
        for q in range(length):
            if sum([self.grid[i+p][j+q] for p in range(length)]) != target_sum:
                return False
        if sum([self.grid[i+p][j+p] for p in range(length)]) != target_sum:
            return False
        if sum([self.grid[i+p][j+length - 1 - p] for p in range(length)]) != target_sum:
            return False
        return True

        