class UnionFind:
    def __init__(self, lands):
        self.size = {land: 1 for land in lands}
        self.parent = {land: land for land in lands}
        self.comp_count = len(lands)

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        node1_parent = self.find(node1)
        node2_parent = self.find(node2)
        if node1_parent == node2_parent:
            return 
        if self.size[node1_parent] > self.size[node2_parent]:
            self.size[node1_parent] += self.size[node2_parent]
            self.parent[node2_parent] = node1_parent
        else:
            self.size[node2_parent] += self.size[node1_parent]
            self.parent[node1_parent] = node2_parent
        self.comp_count -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = set()
        ROW = len(grid)
        COL = len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    lands.add((i, j))
        union_find = UnionFind(lands)
        #print(lands)
        for k, land in enumerate(lands):
            i, j = land
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if next_i < 0 or next_j < 0 or next_i == ROW or next_j == COL:
                    continue
                if (next_i, next_j) in lands:
                    next_land = (next_i, next_j)
                    union_find.union(land, next_land)
        #print(union_find.parent)
        return union_find.comp_count
        
