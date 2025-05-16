class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.out_list = self.init_out_list(numCourses, prerequisites)
        self.topological_sort = []
        for node in range(numCourses):
            if node not in self.out_list:
                continue
            if self.dfs(node, set()) is False:
                return False
        #print(self.topological_sort)
        return len(self.topological_sort) == numCourses

    def dfs(self, node, path):
        if node in path:
            return False
        if node not in self.out_list:
            return True
        path.add(node)
        for ad in self.out_list[node]:
            if self.dfs(ad, path) is False:
                return False
        path.remove(node)
        del self.out_list[node]
        self.topological_sort.append(node)
        return True
        


    def init_out_list(self, n, edges):
        out_list = {i: set() for i in range(n)}
        for node1, node2 in edges:
            out_list[node1].add(node2)
        return out_list