class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.ad_list = self.init_ad_list(prerequisites)
        self.visited = set()
        self.memo = {}
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
        if start in self.memo:
            return self.memo[start]
        visited.add(start)
        for v in self.ad_list[start]:
            has_cycle = self.has_cycle(v, visited)
            if has_cycle:
                visited.remove(start)
                return True
        # To speed up, when you don't find the cycle, you can make it no prerequisites.
        #self.ad_list[start] = []
        self.memo[start] = False
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