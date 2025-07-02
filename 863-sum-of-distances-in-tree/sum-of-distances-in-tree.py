class Solution:
    # base case: 
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ad_list = self.init_ad_list(n, edges)
        self.sub_tree_sizes = [0 for i in range(n)]
        self.n = n
        self.sums = [0 for i in range(n)]
        self.sums[0] = self.get_sum(0)
        self.adjust_sum(0)
        return self.sums
        
    def adjust_sum(self, node, parent=-1):
        if parent != -1:
            self.sums[node] = self.sums[parent] - self.sub_tree_sizes[node] + (self.n - self.sub_tree_sizes[node])
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            self.adjust_sum(ad, node)

    def get_sum(self, src, parent=-1):
        sub_tree_size = 0
        curr_sum = 0
        for ad in self.ad_list[src]:
            if ad == parent:
                continue
            curr_sum += self.get_sum(ad, src)
            sub_tree_size += self.sub_tree_sizes[ad]
        curr_sum += sub_tree_size
        self.sub_tree_sizes[src] = sub_tree_size + 1
        return curr_sum

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1,v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        