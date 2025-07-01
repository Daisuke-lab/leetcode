class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.count = n
    
    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return False
        self.parents[v2_parent] = v1_parent
        self.count -= 1
        return True

class Solution:
    # collect edge
    # sort by cost
    # 
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.collect_edges(points)
        union_find = UnionFind(len(points))
        total_cost = 0
        while edges:
            cost, i, j = heapq.heappop(edges)
            if union_find.union(i, j):
                total_cost += cost
            if union_find.count == 1:
                return total_cost
        return 0


    def collect_edges(self, points):
        edges = []
        for i in range(len(points)-1):
            for j in range(i + 1, len(points)):
                cost = self.get_cost(i, j, points)
                edges.append((cost, i, j))
        heapq.heapify(edges)
        return edges

    def get_cost(self, i, j, points):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])