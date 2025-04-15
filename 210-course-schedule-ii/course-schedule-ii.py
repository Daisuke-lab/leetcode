class Solution:
    # let's collect answer as args
    # let's return has_cycle
    # if you haven't visited yet, you can go through the vertex again and simply extends answer
    # you can still clean up ads once you know it's doesn't have cycle because before it cleans up,it collects result
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.answer = []
        self.learned = set()
        self.ad_list = self.init_ad_list(numCourses, prerequisites)
        for node in self.ad_list:
            if node not in self.learned:
                if self.dfs(node, set()):
                    return []
        
        return self.answer

    def dfs(self, node, visited):
        if node in visited:
            return True
        visited.add(node)
        for ad in self.ad_list[node]:
            if self.dfs(ad, visited):
                return True
        self.ad_list[node] = []
        if node not in self.learned:
            self.answer.append(node)
            self.learned.add(node)
        visited.remove(node)
        return False

    def init_ad_list(self, numCourses, edges):
        ad_list = {i: [] for i in range(numCourses)}
        for v, ad in edges:
            ad_list[v].append(ad)
        return ad_list
        