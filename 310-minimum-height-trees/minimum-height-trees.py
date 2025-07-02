class Solution:
    # init ad_list
    # collected <= n - 2
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ad_list = self.init_ad_list(n, edges)
        edge_node1, _ = self.get_farest_node(0)
        edge_node2, _ = self.get_farest_node(edge_node1)
        path = collections.deque()
        path = self.get_path(edge_node1, edge_node2, path)
        return self.trim(path)

    def trim(self, path):
        while len(path) > 2:
            path.popleft()
            path.pop()
        return list(path)    
    
    def get_path(self, src, dest, path, parent=-1):
        if src == dest:
            path.append(dest)
            return path
        for ad in self.ad_list[src]:
            if ad == parent:
                continue
            new_path = self.get_path(ad, dest, path, src)
            if len(new_path) > 0:
                path.append(src)
                return path
        return path


    def get_farest_node(self, node, parent=-1):
        max_distance = 0
        farest_node = node
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            far_node, distance = self.get_farest_node(ad, node)
            if distance > max_distance:
                max_distance = distance
                farest_node = far_node
        max_distance += 1
        return farest_node, max_distance


    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list

