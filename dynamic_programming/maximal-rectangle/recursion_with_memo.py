class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        print(matrix)
        return self.recursion_with_memo(matrix, 0, 0, len(matrix), len(matrix[0]), {})

    #iが行指定、jが列指定
    def recursion_with_memo(self, matrix, i, j, row_num, col_num, memo):
        key = (i, j, row_num, col_num)
        if key in memo:
            return memo[key]
        if col_num < 1 or row_num < 1:
            return -1
        if col_num == 1 and row_num == 1:
            matrix[i][j] = int(matrix[i][j])
            return matrix[i][j]
        elif row_num == 1:
            left = self.recursion_with_memo(matrix, i, j, row_num, col_num-1, memo)
            right = self.recursion_with_memo(matrix, i, j+1, row_num, col_num-1, memo)
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            memo[key] =  max([left, right, whole])
        elif col_num == 1:
            top = self.recursion_with_memo(matrix, i, j, row_num-1, col_num, memo)
            bottom = self.recursion_with_memo(matrix, i+1, j, row_num-1, col_num, memo)
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            memo[key] =  max([top, bottom, whole])
        else:
            top = self.recursion_with_memo(matrix, i, j, row_num-1, col_num, {})
            bottom = self.recursion_with_memo(matrix, i+1, j, row_num-1, col_num, {})
            left = self.recursion_with_memo(matrix, i, j, row_num, col_num-1, {})
            right = self.recursion_with_memo(matrix, i, j+1, row_num, col_num-1, {})
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            memo[key] =  max([top, bottom, left, right, whole])

        return memo[key]



    def only_one(self, col_i, row_i, col_num, row_num, matrix):
        for i in range(row_i, row_i+row_num):
            if 0 in matrix[i]:
                return False

        return True

