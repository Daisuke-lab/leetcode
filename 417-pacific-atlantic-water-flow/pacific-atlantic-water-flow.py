class Solution:
    # DP
    # you can mark the position as pacific_reachable, atlantic_reachable
    # once you reach the cell, it means you don't have to go through it again
    # you go through every poisition and check if it can be reachable to both oceans
    # Let's define another function
    # the output should be pacific_reachable, atlantic_reachable
    # before propagating, please check the height and index range
    # args would be (i, j)
    # you can cache tab[i][j] = pacific_reachable, atlantic_reachable

    # when it's the same height, the consequence changes based on visited.
    # but at the same time, you want to prevent infinite loop
    # If it's the same height, you can pass ad_reachable as args
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.ROW = len(self.heights)
        self.COL = len(self.heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        for j in range(self.COL):
            first = 0
            last = self.ROW -1
            self.dig(first, j, pacific_reachable)
            self.dig(last, j, atlantic_reachable)
        for i in range(self.ROW):
            first = 0
            last = self.COL - 1
            self.dig(i, first, pacific_reachable)
            self.dig(i, last, atlantic_reachable)
        answer = []
        for i, j in pacific_reachable:
            if (i, j) in atlantic_reachable:
                answer.append([i, j])
        return answer

    def dig(self, i, j, visited):
        if (i, j) in visited:
            return 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited.add((i, j))
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i < 0 or new_i == self.ROW or new_j < 0 or new_j == self.COL:
                continue 
            if self.heights[i][j] > self.heights[new_i][new_j]:
                continue
            self.dig(new_i, new_j, visited)

        