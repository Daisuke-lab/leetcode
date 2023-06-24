class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        set_a = set([])
        set_b = set([])
        visited = []
        for node in range(len(graph)):
            self.recursion(node, set_a, set_b, visited)
        return len(set_a & set_b) == 0

        

    def recursion(self, node, set_a, set_b, visited):
        if node in visited:
            return
        visited.append(node)
        neighbours = self.graph[node]
        set_a.add(node)
        for neighbour in neighbours:
            set_b.add(neighbour)
            self.recursion(neighbour, set_b, set_a, visited)
            