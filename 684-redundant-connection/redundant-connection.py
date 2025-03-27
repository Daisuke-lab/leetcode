class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        self.comp_count = n

    # Find Parent
    def find(self, node):
        while node != self.parent[node]:
            # make your parent to grant parent
            self.parent[node] = self.parent[self.parent[node]]
            # in the next iteration, you check the grantparent
            node = self.parent[node]
        return node

    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)

        # If already connected
        if v1_parent == v2_parent:
            return
        v1_comp_size = self.size[v1_parent]
        v2_comp_size = self.size[v2_parent]
        
        if v1_comp_size > v2_comp_size:
            self.size[v1_parent] += v2_comp_size
            self.parent[v2_parent] = v1_parent
        else:
            self.size[v2_parent] += v1_comp_size
            self.parent[v1_parent] = v2_parent
        self.comp_count -= 1

class Solution:
    # you should for loop backward
    # when you create union find, it should be component of 1
    # how do you operate remove opeartion in union find.
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        for i in range(n-1, -1, -1):
            union_find = UnionFind(n)
            for j in range(n-1, -1, -1):
                if i != j:
                    v1, v2 = edges[j]
                    union_find.union(v1, v2)
                # else:
                #     print("skipping:", edges[j])
            if union_find.comp_count == 1:
                return edges[i]
        