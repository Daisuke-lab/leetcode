class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_heap = [(0, points[0][0], points[0][1])]
        total_cost = 0
        while min_heap:
            cost, i, j = heapq.heappop(min_heap)
            if (i, j) in visited:
                continue
            if len(visited) == len(points):
                break
            total_cost += cost
            visited.add((i, j))
            for next_i, next_j in points:
                if (next_i, next_j) in visited:
                    continue
                cost = abs(next_i - i) + abs(next_j - j)
                heapq.heappush(min_heap, (cost, next_i, next_j))
        return total_cost