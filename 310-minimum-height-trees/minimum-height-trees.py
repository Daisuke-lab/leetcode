class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        self.ad_list = self.init_ad_list(n, edges)
        edge_node,_ = self.get_farest_node(0)
        edge_node2,_ = self.get_farest_node(edge_node)
        #print(edge_node, edge_node2)
        path = self.collect_path(edge_node, edge_node2)
        #print(path)

        #print(centroids)
        m = len(path) // 2
        if len(path) % 2 == 1:
            return [path[m]]
        else:
            return [path[m - 1], path[m]]

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        
    def get_farest_node(self, node, parent=None):
        farthest_node = node
        max_distance = 0
        for ad in self.ad_list[node]:
            if ad != parent:
                far_node, distance = self.get_farest_node(ad, node)
                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    farthest_node = far_node
        return farthest_node, max_distance

    def collect_path(self, v1, v2, parent=None):
        #print(v1, v2)
        if v1 == v2:
            return [v2]
        for ad in self.ad_list[v1]:
            if ad == parent:
                continue
            path = self.collect_path(ad, v2, v1)
            if len(path) != 0:
                path.append(v1)
                return path
        return []
        

        