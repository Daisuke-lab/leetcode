class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.out_list = self.init_out_list(numCourses, prerequisites)
        self.in_list = self.init_in_list(numCourses, prerequisites)
        queue = self.collect_zero_incoming_vertices(self.in_list)
        topological_sort = []
        while queue:
            node = queue.popleft()
            topological_sort.append(node)
            for ad in self.out_list[node]:
                self.in_list[ad].remove(node)
                if len(self.in_list[ad]) == 0:
                    queue.append(ad)

        return len(topological_sort) == numCourses
        

    def find_cycle(self, node, visited):
        if node in visited:
            return True
        visited.add(node)
        for ad in self.ad_list[node]:
            if self.find_cycle(ad, visited):
                return True
        self.ad_list[node] = []
        visited.remove(node)
        return False

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
        
