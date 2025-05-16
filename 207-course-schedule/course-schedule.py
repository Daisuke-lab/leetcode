class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.out_list = self.init_out_list(numCourses, prerequisites)
        self.in_list = self.init_in_list(numCourses, prerequisites)
        queue = self.collect_zero_incoming_vertices(self.in_list)
        self.topological_sort = []
        self.visited = set()
        while queue:
            node = queue.popleft()
            if node in self.visited:
                continue
            if self.dfs(node, set()) is False:
                return False
        #print(self.topological_sort)
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
        self.topological_sort.append(node)
        self.visited.add(node)
        return True
        


    def init_out_list(self, n, edges):
        out_list = {i: set() for i in range(n)}
        for node1, node2 in edges:
            out_list[node1].add(node2)
        return out_list

    def init_in_list(self, n, edges):
        in_list = {i: set() for i in range(n)}
        for node1, node2 in edges:
            in_list[node2].add(node1)
        return in_list

    def collect_zero_incoming_vertices(self, in_list):
        queue = collections.deque()
        for node in in_list.keys():
            if len(in_list[node]) == 0:
                queue.append(node)

        return queue
        
