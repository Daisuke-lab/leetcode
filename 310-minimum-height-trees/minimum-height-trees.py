class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ad_list = self.init_ad_list(n, edges)
        # self.memo[i][0]: tallest subtree height from node i (max height from children)
        # self.memo[i][1]: second tallest subtree height from node i
        self.memo = [[0] * 2 for _ in range(n)]
        self.build_heights_to(0)
        self.build_heights_from(0)
        min_height = min([self.memo[i][0] for i in range(n)])
        answer = [i for i in range(n) if self.memo[i][0] == min_height]
        return answer
        
    def build_heights_to(self, node, parent=None):
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            height = self.build_heights_to(ad, node) + 1
            if height > self.memo[node][0]:
                self.memo[node][1] = self.memo[node][0]
                self.memo[node][0] = height
            elif height > self.memo[node][1]:
                self.memo[node][1] = height
        return self.memo[node][0]


    def build_heights_from(self, node, parent=None, curr_height=0):
        if curr_height > self.memo[node][0]:
            self.memo[node][1] = self.memo[node][0]
            self.memo[node][0] = curr_height
        elif curr_height > self.memo[node][1]:
            self.memo[node][1] = curr_height

        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            if self.memo[node][0] == 1 + self.memo[ad][0]:
                next_height = 1 + self.memo[node][1]
            else:
                next_height = 1 + self.memo[node][0]
            self.build_heights_from(ad, node, next_height)


    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        

        