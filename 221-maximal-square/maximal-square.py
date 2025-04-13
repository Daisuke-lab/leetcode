class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = self.generate_height_matrix(matrix)
        max_area = 0
        for row in matrix:
            area = self.get_largest_square(row)
            max_area = max(area, max_area)
        return max_area

    def get_largest_square(self, heights):
        i = 0
        max_area = 0
        stack = []
        for i in range(len(heights)):
            j = i
            while stack and stack[-1][1] > heights[i]:
                j, height = stack.pop()
                width = i - j
                length = min(width, height)
                max_area = max(max_area, length**2)
            heights[j] = heights[i]
            stack.append((j, heights[i]))
        while stack:
            j, height = stack.pop()
            width = i - j + 1
            length = min(width, height)
            max_area = max(max_area, length**2)

            
        return max_area

    def generate_height_matrix(self, matrix):
        ROW = len(matrix)
        COL = len(matrix[0])
        height_matrix = [[0 for j in range(COL)] for i in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                matrix[i][j] = int(matrix[i][j])
                if i != 0 and matrix[i][j] > 0:
                    matrix[i][j] += matrix[i-1][j]
        return matrix