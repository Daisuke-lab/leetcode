class Solution:
    # It's graph problem, but you can not simply connect two components
    # It has to be k connections.
    # 
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        self.ad_list = self.init_ad_list(properties, k)
        self.visited = set()
        count = 0
        for v in self.ad_list.keys():
            if v not in self.visited:
                count += 1
                self.dfs(v, None)
        #print(self.ad_list)
        return count

    def dfs(self, src, parent):
        if src in self.visited:
            return 
        self.visited.add(src)
        for v in self.ad_list[src]:
            if v != parent:
                self.dfs(v, src)
        
                    

    def init_ad_list(self, properties, k):
        ad_list = {i: set() for i in range(len(properties))}
        for i in range(0, len(properties) - 1):
            for j in range(i+1, len(properties)):
                if len(set(properties[i]) & set(properties[j])) >= k:
                    ad_list[i].add(j)
                    ad_list[j].add(i)
        return ad_list
        