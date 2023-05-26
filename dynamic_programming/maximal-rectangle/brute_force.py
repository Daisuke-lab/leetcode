class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        return self.brute_force(matrix)

    def brute_force(self, matrix):
        max_sum = int(matrix[0][0])
        row_len = len(matrix)
        col_len = len(matrix[0])
        col_num = 1
        row_num = 1
        while row_num <= row_len:
            for col_i in range(col_len - col_num + 1):
                for row_i in range(row_len - row_num + 1):
                    temp = row_num * col_num
                    if self.only_one(col_i, row_i, col_num, row_num, matrix) and temp > max_sum:
                        max_sum = temp
            if col_num == col_len:
                col_num = 1
                row_num += 1
            else:
                col_num += 1
        return max_sum

            


    def only_one(self, col_i, row_i, col_num, row_num, matrix):
        for i in range(col_i, col_i+col_num):
            for j in range(row_i, row_i+row_num):
                if matrix[j][i] == "0":
                    return False

        return True
