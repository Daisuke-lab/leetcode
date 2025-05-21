class Solution:
    # undirected graph
    # you want to create ad_list
    # value_map[(edge)] = value
    
    #  how do you detect cycle ? => just have path with dfs
    #  if you can not reach to the destination, it is also -1
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.ad_list = self.init_ad_list(equations)
        self.value_map = self.init_value_map(equations, values)
        answer = []
        for src, dest in queries:
            result = self.dfs(src, dest, set())
            answer.append(result)
        return answer

    def dfs(self, src, dest, visited):
        if src not in self.ad_list or dest not in self.ad_list:
            return - 1.0
        if src == dest:
            return 1.0
        elif src in visited:
            return -1.0
        visited.add(src)
        for ad in self.ad_list[src]:
            result = self.dfs(ad, dest, visited)
            if result != - 1.0:
                return result * self.value_map[(src, ad)]
        return -1.0
    def init_ad_list(self, edges):
        ad_list = {}
        for v1, v2 in edges:
            v1_ads = ad_list.get(v1, set())
            v2_ads = ad_list.get(v2, set())
            v1_ads.add(v2)
            v2_ads.add(v1)
            ad_list[v1] = v1_ads
            ad_list[v2] = v2_ads
        return ad_list

    def init_value_map(self, edges, values):
        value_map = {}
        for i, edge in enumerate(edges):
            v1, v2 = edge
            edge = (v1, v2)
            reverse_edge = (v2, v1)
            value_map[edge] = values[i]
            value_map[reverse_edge] = 1/values[i]
        return value_map
        