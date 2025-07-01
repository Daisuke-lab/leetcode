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
    # Critical Edge
    # do Kruscal as normal
    # remove one edge and see if it changes the total cost, If so, that is critical

    # Pseudo Edge
    # there might be some edges that never appears even if you delete a critical edge
    # => you can force use the edge and then see what is going to happen
    # 
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical_edges = set()
        pseudo_critical_edges = set()
        edges, index_map = self.sort_edges_with_map(edges)
        right_mst_cost = self.create_mst(n, edges)
        for i in range(len(edges)):
            original_index = index_map[i]
            mst_cost = self.create_mst(n, edges, avoidant_edge=edges[i])
            if mst_cost != right_mst_cost:
                critical_edges.add(original_index)
            else:
                mst_cost = self.create_mst(n, edges, must_edge=edges[i])
                if mst_cost == right_mst_cost:
                    pseudo_critical_edges.add(original_index)
        return [list(critical_edges), list(pseudo_critical_edges)]

    def create_mst(self, n, edges, must_edge=None, avoidant_edge=None):
        union_find = UnionFind(n)
        total_cost = 0
        if must_edge:
            union_find.union(must_edge[0], must_edge[1])
            total_cost += must_edge[2]
        for edge in edges:
            if avoidant_edge and edge[0] == avoidant_edge[0] and edge[1] == avoidant_edge[1]:
                continue
            if union_find.union(edge[0], edge[1]):
                total_cost += edge[2]
            if union_find.count ==1:
                return total_cost
        return total_cost

    def sort_edges_with_map(self, edges):
        indexed_edges = [edge + [i] for i, edge in enumerate(edges)]
        indexed_edges.sort(key=lambda edge: edge[2])
        index_map = {i: edge[-1] for i, edge in enumerate(indexed_edges)}
        sorted_edges = [[a,b,c] for a,b,c, original_index in indexed_edges]
        return sorted_edges, index_map