class Solution:
    # What is difficult?
    # You wouldn't know if it's newly created 0 or not
    # Let' change it to -1 first
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.ROW = len(matrix)
        self.COL = len(matrix[0])
        self.matrix = matrix
        for i in range(self.ROW):
            for j in range(self.COL):
                if matrix[i][j] == 0:
                    self.turnaround(i, j, "")
        
        for i in range(self.ROW):
            for j in range(self.COL):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0


    def turnaround(self, i, j, direction):
        if i < 0 or j < 0 or i == self.ROW or j == self.COL:
            return
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = float("inf")
            self.turnaround(i-1, j, "up")
            self.turnaround(i+1, j, "down")
            self.turnaround(i, j-1, "left")
            self.turnaround(i, j+1, "right")
        else:
            self.matrix[i][j] = float("inf")
            if direction == "up":
                self.turnaround(i-1, j, "up")
            elif direction == "down":
                self.turnaround(i+1, j, "down")
            elif direction == "left":
                self.turnaround(i, j-1, "left")
            else:
                self.turnaround(i, j+1, "right")
        
        