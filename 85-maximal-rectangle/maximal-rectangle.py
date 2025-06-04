class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histograms = self.generate_histogram(matrix)
        max_rectangle = 0
        for histogram in histograms:
            print(histogram)
            max_rectangle = max(self.get_largest_rectangle(histogram), max_rectangle)
        return max_rectangle


    def get_largest_rectangle(self, histogram):
        stack = []
        largest_rectangle = 0
        for j in range(len(histogram)):
            i = None
            while stack and histogram[stack[-1]] > histogram[j]:
                i = stack.pop()
                width = j - i
                height = histogram[i]
                largest_rectangle = max(largest_rectangle, width * height)
                histogram[i] = histogram[j]
            if i is not None:
                stack.append(i)
            stack.append(j)
        while stack:
            i = stack.pop()
            j = len(histogram)
            width = j - i
            height = histogram[i]
            largest_rectangle = max(largest_rectangle, width * height)
        
        return largest_rectangle

    def generate_histogram(self, matrix):
        ROW = len(matrix)
        COL = len(matrix[0])
        histograms = [[
            0 for j in range(COL)]
            for i in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                matrix[i][j] = int(matrix[i][j])
                if i == 0:
                    histograms[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    histograms[i][j] = 0
                else:
                    histograms[i][j] = histograms[i-1][j] + matrix[i][j]
        return histograms