class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        memo = [[
            0 for j in range(COL)]
            for i in range(ROW)]
        max_length = 0
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == "0":
                    continue
                elif i == 0 or j == 0:
                    memo[i][j] = int(matrix[i][j])
                else:
                    ensured_length = min(memo[i-1][j], memo[i][j-1])
                    potential_length = ensured_length + 1
                    if matrix[i-(potential_length-1)][j-(potential_length-1)] == "1":
                        memo[i][j] = potential_length
                    else:
                        memo[i][j] = max(1, ensured_length)
                max_length = max(max_length, memo[i][j])
        return max_length * max_length