class Solution:
    # let's collect answer as args
    # let's return has_cycle
    # if you haven't visited yet, you can go through the vertex again and simply extends answer
    # you can still clean up ads once you know it's doesn't have cycle because before it cleans up,it collects result
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.answer = []
        self.ad_list = self.init_ad_list(numCourses, prerequisites)
        self.visited = set()
        print(self.ad_list)
        for v in self.ad_list.keys():
            if v not in self.visited:
                has_cycle = self.has_cycle(v, set())
                if has_cycle:
                    return []

        return list(self.answer)
    
    def has_cycle(self, src, curr):
        #print(src)
        if src in curr:
            return True
        curr.add(src)
        has_cycle = False
        for v in self.ad_list[src]:
            has_cycle = self.has_cycle(v, curr)
            if has_cycle:
                return True
        if src not in self.visited:
            self.answer.append(src)
        self.visited.add(src)
        curr.remove(src)
        self.ad_list[src] = []
        return False

    def init_ad_list(self, numCourses, edges):
        ad_list = {i: [] for i in range(numCourses)}
        for v, ad in edges:
            ad_list[v].append(ad)
        return ad_list
        