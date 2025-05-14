class Solution:
    # DP 
    # each cell holds max height, max width
    # if current cell is 1, you can copy the memo[i][j - 1][width] + 1 as width
    # if current cell is 1 and width == memo[i - 1][j], you can copy memo[i-1][j][height] + 1
    # 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.ROW = len(matrix)
        self.COL = len(matrix[0])
        histgrams = self.generate_histgrams(matrix)
        print(histgrams)
        max_area = 0
        for histgram in histgrams:
            area = self.find_max_area(histgram)
            max_area = max(max_area, area)
        return max_area

    def find_max_area(self, histgram):
        stack = []
        max_area = 0
        for i, height in enumerate(histgram):
            prev_i = None
            while len(stack) > 0 and histgram[stack[-1]] > height:
                prev_i = stack.pop()
                width = i - prev_i
                prev_height = histgram[prev_i]
                area = width * prev_height
                max_area = max(max_area, area)
            if prev_i is not None:
                stack.append(prev_i)
                histgram[prev_i] = height

            stack.append(i)
        i = len(histgram)
        while stack:
            prev_i = stack.pop()
            width = i - prev_i
            height = histgram[prev_i]
            area = width * height
            max_area = max(max_area, area)
        return max_area

    def generate_histgrams(self, matrix):
        histgrams = [[
            0 for j in range(self.COL)]
            for i in range(self.ROW)]
        for i in range(self.ROW):
            for j in range(self.COL):
                matrix[i][j] = int(matrix[i][j])
                if i == 0:
                    histgrams[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 0:
                        histgrams[i][j] = 0
                    else:
                        histgrams[i][j] = histgrams[i-1][j] + matrix[i][j]
        return histgrams
        