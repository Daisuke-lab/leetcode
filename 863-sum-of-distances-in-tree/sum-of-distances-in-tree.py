class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ad_list = self.init_ad_list(n, edges)
        self.m = len(edges)
        self.n = n
        count_map, distance_map = self.build_distance_map_to(0)
        self.build_universal_distance_map(0, count_map, distance_map)
        return self.distance_map


    def build_universal_distance_map(self, node, count_map, distance_map):
        self.count_map = count_map
        self.distance_map = distance_map
        self.build_distance_map_from(0)
    
    def build_distance_map_from(self, node, parent=None):
        farther_node_counts = self.n - self.count_map[node]
        closer_node_counts = self.count_map[node]
        if parent is not None:
            new_distance = self.distance_map[parent] + farther_node_counts - closer_node_counts
            self.distance_map[node] = new_distance
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            self.build_distance_map_from(ad, node)
            

    def build_distances_to(self, node, parent=None):
        node_count = 1
        distance_sum = 0
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            count, distance = self.build_distances_to(ad, node)
            node_count += count
            distance_sum += distance
        self.count_map[node] = node_count
        curr_distance = distance_sum + node_count - 1
        self.distance_map[node] = curr_distance
        return node_count, self.distance_map[node]
        
    def build_distance_map_to(self, node):
        self.count_map = [0 for i in range(self.n)]
        self.distance_map = [0 for i in range(self.n)]
        self.build_distances_to(node)
        return self.count_map, self.distance_map


                

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        