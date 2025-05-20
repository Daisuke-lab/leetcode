class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.distances = [0 for i in range(n)]


    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, v1, v2, distance):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return False
        if self.distances[v1_parent] > self.distances[v2_parent]:
            self.parents[v2_parent] = v1_parent
            self.distances[v1_parent] += self.distances[v2_parent] + distance
        else:
            self.parents[v1_parent] = v2_parent
            self.distances[v2_parent] += self.distances[v1_parent] + distance
        return True 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        self.points = points
        union_find = UnionFind(n)
        edges = sorted(self.collect_edges(n), key=lambda edge: edge[2])
        for v1, v2, distance in edges:
            union_find.union(v1, v2, distance)
        return union_find.distances[union_find.find(0)]
        

    def collect_edges(self, n):
        edges = []
        for i in range(n-1):
            for j in range(i+1, n):
                distance = self.get_distance(i, j) 
                edges.append((i, j, distance))
        return edges

    def get_distance(self, v1, v2):
        return abs(self.points[v1][0] - self.points[v2][0]) + abs(self.points[v1][1] - self.points[v2][1])
        