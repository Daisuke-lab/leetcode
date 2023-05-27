class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        print(matrix)
        return self.recursion(matrix, 0, 0, len(matrix), len(matrix[0]))

    #iが行指定、jが列指定
    def recursion(self, matrix, i, j, row_num, col_num):
        if col_num < 1 or row_num < 1:
            return -1
        if col_num == 1 and row_num == 1:
            matrix[i][j] = int(matrix[i][j])
            return matrix[i][j]
        elif row_num == 1:
            left = self.recursion(matrix, i, j, row_num, col_num-1)
            right = self.recursion(matrix, i, j+1, row_num, col_num-1)
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            return max([left, right, whole])
        elif col_num == 1:
            top = self.recursion(matrix, i, j, row_num-1, col_num)
            bottom = self.recursion(matrix, i+1, j, row_num-1, col_num)
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            return max([top, bottom, whole])
        else:
            top = self.recursion(matrix, i, j, row_num-1, col_num)
            bottom = self.recursion(matrix, i+1, j, row_num-1, col_num)
            left = self.recursion(matrix, i, j, row_num, col_num-1)
            right = self.recursion(matrix, i, j+1, row_num, col_num-1)
            if self.only_one(j, i, col_num, row_num, matrix):
                whole = col_num * row_num
            else:
                whole = 0
            return max([top, bottom, left, right, whole])



    def only_one(self, col_i, row_i, col_num, row_num, matrix):
        for i in range(col_i, col_i+col_num):
            for j in range(row_i, row_i+row_num):
                if matrix[j][i] == 0:
                    return False

        return True



            
