class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        grid = [[0 if j != len(t) else 1 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
        
        for i in range(len(s) -1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    grid[i][j] = grid[i+1][j+1] + grid[i+1][j]
                else:
                    grid[i][j] = grid[i+1][j]

        return grid[0][0]