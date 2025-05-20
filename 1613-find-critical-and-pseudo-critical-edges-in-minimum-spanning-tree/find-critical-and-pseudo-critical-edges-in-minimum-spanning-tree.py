class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return 
        self.parents[v2_parent] = v1_parent


class Solution:
    # try kruscal usual
    # remove 1 edge in the inital result and try again
    # if mst changes, the missing edge is critical
    # if not, it is psuedo critical
    #         any of edge in the same size mst, you should be in the edge set to examine
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        original_edges = edges
        self.index_map, edges = self.sort_edges(edges)
        mst_edges, min_cost = self.kruscal(n, edges)
        criticals = set()
        pseudo_criticals = set()
        for i, edge in enumerate(edges):
            potential_mst_edges, cost = self.kruscal(n, edges, edge, False)
            if cost != min_cost:
                criticals.add(self.index_map[i])
            potential_mst_edges, cost = self.kruscal(n, edges, edge, True)
            if cost == min_cost:
                pseudo_criticals.add(self.index_map[i])


        pseudo_criticals = pseudo_criticals - criticals
        return [list(criticals), list(pseudo_criticals)]

    def kruscal(self, n, edges, special_edge=None, include=False):
        union_find = UnionFind(n)
        min_cost = 0
        mst_edges = set()
        if include:
            min_cost += special_edge[2]
            union_find.union(special_edge[0], special_edge[1])
        for i, edge in enumerate(edges):
            if union_find.find(edge[0]) == union_find.find(edge[1]):
                continue
            if not include and special_edge and edge[0] == special_edge[0] and edge[1] == special_edge[1]:
                continue
            min_cost += edge[2]
            union_find.union(edge[0], edge[1])
            mst_edges.add(self.index_map[i])
        return mst_edges, min_cost

    def sort_edges(self, edges):
        pairs = [(i, edge) for i, edge in enumerate(edges)]
        pairs.sort(key=lambda pair: pair[1][2])
        index_map = {i: pair[0] for i, pair in enumerate(pairs)}
        sorted_edges = [pair[1] for pair in pairs]
        return index_map, sorted_edges
        
        