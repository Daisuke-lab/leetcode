class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = [(0, 0)]
        visited = set()
        cost = 0
        while min_heap:
            distance, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            cost += distance
            for j in range(len(points)):
                if j == i or j in visited:
                    continue
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(min_heap, (distance, j))
        return cost

        