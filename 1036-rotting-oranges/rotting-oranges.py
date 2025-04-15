class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = set()
        rotten_oranges = set()
        ROW = len(grid)
        COL = len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    rotten_oranges.add((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges.add((i, j))
        
        minutes = 0
        while rotten_oranges:
            newly_rotten_oranges = set()
            for i, j in rotten_oranges:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if next_i < 0 or next_j < 0 or next_i == ROW or next_j == COL:
                        continue
                    if (next_i, next_j) in fresh_oranges:
                        fresh_oranges.remove((next_i, next_j))
                        newly_rotten_oranges.add((next_i, next_j))
            if len(newly_rotten_oranges) > 0:
                minutes += 1
            rotten_oranges = newly_rotten_oranges
        return minutes if len(fresh_oranges) == 0 else -1
            

                


        