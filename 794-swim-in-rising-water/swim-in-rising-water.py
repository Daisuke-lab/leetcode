class Solution:
    # goes to the 4 directions
    # heap by height, i, j
    # 
    def swimInWater(self, grid: List[List[int]]) -> int:
      visited = set()
      ROW = len(grid)
      COL = len(grid[0])
      heap = [(-1, 0, 0)]
      while heap:
        curr_max, i, j = heapq.heappop(heap)
        if (i, j) in visited:
            continue
        if i < 0 or j < 0 or i >= ROW or j >= COL:
            continue
        if (i, j) == (ROW-1, COL -1):
            return max(curr_max, grid[i][j])
        visited.add((i, j))
        heapq.heappush(heap, (max(curr_max, grid[i][j]), i-1, j))
        heapq.heappush(heap, (max(curr_max, grid[i][j]), i+1, j))
        heapq.heappush(heap, (max(curr_max, grid[i][j]), i, j-1))
        heapq.heappush(heap, (max(curr_max, grid[i][j]), i, j+1))

        