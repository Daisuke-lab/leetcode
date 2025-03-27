class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return
        v1_comp_size = self.size[v1_parent]
        v2_comp_size = self.size[v2_parent]
        if v1_comp_size > v2_comp_size:
            self.parent[v2_parent] = v1_parent
            self.size[v1_parent] += v2_comp_size
        else:
            self.parent[v1_parent] = v2_parent
            self.size[v2_parent] += v1_comp_size


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_find = UnionFind(n)
        for v1, v2 in edges:
            union_find.union(v1, v2)
        source_parent = union_find.find(source)
        dest_parent = union_find.find(destination)
        return source_parent == dest_parent
        

        