class Solution:
    # find the path that min(routes) is the smallest
    # DP
    # n^3

    # 
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.ROW = len(grid)
        self.COL = len(grid[0])
        dj_matrix = [[float("inf") for j in range(self.COL)] for i in range(self.ROW)]
        dj_matrix[0][0] = grid[0][0]
        min_heap = [(grid[0][0],0, 0)]
        visited = set()
        while min_heap:
            max_val, i, j = heapq.heappop(min_heap)
            if (i, j) in visited:
                continue
            
            if i == self.ROW - 1 and j == self.COL - 1:
                return max_val
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited.add((i, j))
            
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if next_i < 0 or next_j < 0 or next_i == self.ROW or next_j == self.COL:
                    continue
                if dj_matrix[next_i][next_j] > max(max_val, grid[next_i][next_j]):
                        dj_matrix[next_i][next_j] = max(max_val, grid[next_i][next_j])
                if (next_i, next_j) not in visited:
                    next_max_val = max(grid[next_i][next_j], max_val)
                    heapq.heappush(min_heap, (next_max_val, next_i, next_j))

    
        


        