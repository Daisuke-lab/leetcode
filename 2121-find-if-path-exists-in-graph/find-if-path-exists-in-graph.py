class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.ad_list = self.init_ad_list(edges)
        self.visited = set()
        return self.dfs(source, destination)
        

    def dfs(self, src, dest):
        if src == dest:
            return True
        if src in self.visited:
            return False
        self.visited.add(src)
        for v in self.ad_list[src]:
            result = self.dfs(v, dest)
            if result:
                return True
        return False

    def init_ad_list(self, edges):
        ad_list = defaultdict(list)
        for v1, v2 in edges:
            ad_list[v1].append(v2)
            ad_list[v2].append(v1)
        return ad_list
        