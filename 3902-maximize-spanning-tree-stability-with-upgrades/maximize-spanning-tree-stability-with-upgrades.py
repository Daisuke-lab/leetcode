class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.count = n
    
    def find(self, node):
        while self.parents[node] != node:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return False
        self.parents[v1_parent] = v2_parent
        self.count -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges, unmust_edges = self.separate_edges(edges)
        unmust_edges.sort(key=lambda edge: edge[2], reverse=True)
        union_find = UnionFind(n)
        min_strength = float("inf")
        for v1, v2, strength in must_edges:
            if union_find.union(v1, v2):
                min_strength = min(min_strength, strength)
            else:
                return -1
        for v1, v2, strength in unmust_edges:
            if union_find.union(v1, v2):
                strength = strength*2 if (union_find.count) <= k and k> 0 else strength
                min_strength = min(min_strength, strength)
            if union_find.count == 1:
                return min_strength
        if union_find.count == 1:
            return min_strength
        else:
            return -1

    def separate_edges(self, edges):
        must_edges = []
        unmust_edges = []
        for v1, v2, strength, must in edges:
            if must == 1:
                must_edges.append((v1, v2,strength))
            else:
                unmust_edges.append((v1, v2, strength))
        return must_edges, unmust_edges