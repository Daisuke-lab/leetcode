class Solution:
    # you keep matrix size memo
    # if you are 0, it's 0
    # if it is 1
    # => 1. you take the min of top and left
    # => 2. potential length would be + 1 to that
    # => 3. check diagonal line to check if you can expand it or not
    # get the max
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_length = 0
        ROW = len(matrix)
        COL = len(matrix[0])
        memo = [[
            0 for i in range(COL)]
            for j in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                matrix[i][j] = int(matrix[i][j]) 
                if i == 0 or j == 0:
                    memo[i][j] = matrix[i][j]
                    max_length = max(max_length, memo[i][j])
                elif matrix[i][j] == 0:
                    memo[i][j] = 0
                else:
                    min_length = min(memo[i-1][j], memo[i][j-1])
                    potential_length = min_length + 1
                    if matrix[i - potential_length + 1][j - potential_length + 1] == 1:
                        memo[i][j] = potential_length
                    else:
                        memo[i][j] = max(min_length, 1)
                    max_length = max(max_length, memo[i][j])
        return max_length**2