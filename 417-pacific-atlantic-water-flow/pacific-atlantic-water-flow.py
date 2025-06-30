class Solution:
    # from the edge to the top
    # you keep expanding it as long as 
    # it is higher than or equal to prev
    # it is not labeled yet
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.ROW = len(heights)
        self.COL = len(heights[0])
        self.memo = [[
            0 for i in range(self.COL)]
            for j in range(self.ROW)]
        self.answer = []
        for i in range(self.ROW):
            self.flow(i, 0, -1, True)
            self.flow(i, self.COL - 1, -1, False)
        for j in range(self.COL):
            self.flow(0, j, -1, True)
            self.flow(self.ROW - 1, j, -1, False)
        return self.answer


    def flow(self, i, j, prev, is_pacific):
        if i < 0 or j < 0 or i >= self.ROW or j >= self.COL:
            return 
        elif prev > self.heights[i][j]:
            return
        elif self.memo[i][j] == 3:
            return
        elif is_pacific and self.memo[i][j] == 1:
            return
        elif not is_pacific and self.memo[i][j] == 2:
            return
        
        if self.memo[i][j] == 0:
            self.memo[i][j] = 1 if is_pacific else 2
        elif self.memo[i][j] == 1 and not is_pacific:
            self.memo[i][j] = 3
            self.answer.append([i, j])
        elif self.memo[i][j] == 2 and is_pacific:
            self.memo[i][j] = 3
            self.answer.append([i, j])
        self.flow(i-1, j, self.heights[i][j], is_pacific)
        self.flow(i+1, j, self.heights[i][j], is_pacific)
        self.flow(i, j-1, self.heights[i][j], is_pacific)
        self.flow(i, j+1, self.heights[i][j], is_pacific)

        

