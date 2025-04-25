class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        ROW = len(grid)
        COL = len(grid[0])
        self.grid = grid
        if ROW < 3 or COL < 3:
            return 0
        for i in range(ROW-2):
            for j in range(COL - 2):
                if self.is_magic_square(i, j, 3, 15):
                    count +=1
        return count


    def is_magic_square(self, i, j, length, target_sum):
        num_set = set()
        for p in range(length):
            for q in range(length):
                if self.grid[i+p][j+q] in num_set or self.grid[i+p][j+q] > 9 or self.grid[i+p][j+q] < 1:
                    return False
                num_set.add(self.grid[i+p][j+q])
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
                