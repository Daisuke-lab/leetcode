class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.out_list = self.init_out_list(numCourses, prerequisites)
        self.topological_sort = []
        self.visited = set()
        for node in range(numCourses):
            if node in self.visited:
                continue
            self.dfs(node, set())
        return len(self.topological_sort) == numCourses

    def dfs(self, node, path):
        if node in path:
            return False
        if node in self.visited:
            return True
        path.add(node)
        for ad in self.out_list[node]:
            if self.dfs(ad, path) is False:
                return False
        path.remove(node)
        self.out_list[node] = set()
        self.topological_sort.append(node)
        self.visited.add(node)
        return True
        


    def init_out_list(self, n, edges):
        out_list = {i: set() for i in range(n)}
        for node1, node2 in edges:
            out_list[node1].add(node2)
        return out_list

        
