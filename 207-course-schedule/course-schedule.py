class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.ad_list = self.init_ad_list(prerequisites)
        for node in self.ad_list:
            found = self.find_cycle(node, set())
            if found:
                return False
        return True

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

    def init_ad_list(self, edges):
        ad_list = {}
        for node1, node2 in edges:
            node1_ads = ad_list.get(node1, [])
            node1_ads.append(node2)
            ad_list[node1] = node1_ads
            ad_list[node2] = ad_list.get(node2, [])
        return ad_list
        
