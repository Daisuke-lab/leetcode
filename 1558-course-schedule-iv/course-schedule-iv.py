class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.ad_list = self.init_ad_list(numCourses, prerequisites)
        #print(self.ad_list)
        answer = []
        self.memo = {}
        for src, dest in queries:
            answer.append(self.find_path(src, dest, set()))
        return answer


    def find_path(self, src, dest, path):
        if src == dest:
            return True
        if src in path:
            return False
        if (src, dest) in self.memo:
            return self.memo[(src, dest)]
        path.add(src)
        result = False
        for ad in self.ad_list[src]:
            if self.find_path(ad, dest, path):
                result = True
                break
        path.remove(src)
        self.memo[(src, dest)] = result
        return result
        


    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            # main course -> prerequisites
            ad_list[v1].add(v2)
        return ad_list
        