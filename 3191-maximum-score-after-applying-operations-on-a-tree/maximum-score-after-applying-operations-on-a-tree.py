class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        self.values = values
        self.ad_list = self.init_ad_list(n, edges)
        return self.dfs(0, None)[0]

    def dfs(self, node, parent):
        safe_result = 0
        unsafe_result = 0
        for ad in self.ad_list[node]:
            if ad != parent:
                child_safe_result, child_unsafe_result = self.dfs(ad, node)
                safe_result += child_safe_result
                unsafe_result += child_unsafe_result
        # case 1: remain curr and take unsafe_result as safe
        # case2: take curr and add it to the safe result
        if unsafe_result != 0:
            safe_result = max(safe_result + self.values[node], unsafe_result)
        unsafe_result += self.values[node]
        return safe_result, unsafe_result

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        