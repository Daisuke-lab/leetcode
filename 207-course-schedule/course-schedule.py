class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.ad_list = self.init_ad_list(prerequisites)
        #print(self.ad_list)
        self.visited = set()
        for v in self.ad_list.keys():
            if v not in self.visited:
                has_cycle = self.has_cycle(v, set())
                if has_cycle:
                    return False
        return True


    def has_cycle(self, start, visited):
        self.visited.add(start)
        if start in visited:
            return True
        visited.add(start)
        for v in self.ad_list[start]:
            has_cycle = self.has_cycle(v, visited)
            if has_cycle:
                visited.remove(start)
                return True
        self.ad_list[start] = []
        visited.remove(start)
        return False

    def init_ad_list(self, edges):
        ad_list = {}
        for v1, v2 in edges:
            v1_list = ad_list.get(v1, [])
            v1_list.append(v2)
            ad_list[v1] = v1_list
            ad_list[v2] = ad_list.get(v2, []) 
        return ad_list