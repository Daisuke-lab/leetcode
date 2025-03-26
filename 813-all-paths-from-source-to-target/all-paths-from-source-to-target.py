class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.answer = []
        src = 0
        dst = len(graph) - 1
        self.ad_list = self.init_ad_list(graph)
        self.dfs(src, dst, [], set())
        return self.answer

    def dfs(self, src, dst, curr, visited):
        curr.append(src)
        if src in visited:
            return 
        if src == dst:
            self.answer.append(curr.copy())
        visited.add(src)
        for v in self.ad_list[src]:
            self.dfs(v, dst, curr, visited)
        curr.pop()
        visited.remove(src)

    
    def init_ad_list(self, graph):
        ad_list = {}
        for v, ads in enumerate(graph):
            ad_list[v] = ads
        return ad_list
        