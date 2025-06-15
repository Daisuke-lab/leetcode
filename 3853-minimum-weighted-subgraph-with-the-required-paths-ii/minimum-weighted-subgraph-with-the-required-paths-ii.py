class Solution:
    # you need to keep distance, node in binary lifting
    # it doesn't matter which node can be considered as root
    # how do we get lowest common ancestor so quickly => use binary lifting
    # what is node? what is exponent? what is value in this example?
    # node can be as it is. value is LCA (node).
    # is it just 2D array? 
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.n = len(edges) + 1
        self.m = len(edges)
        self.ad_list = self.init_ad_list(self.n, edges)
        self.levels, self.weights, self.ancestors = self.init_binary_lifting(self.n)
        distances = []
        for (v1, v2, v3) in queries:
            distance = 0
            distance += self.get_distance(v1, v2)
            distance += self.get_distance(v1, v3)
            distance += self.get_distance(v2, v3)
            distance /= 2
            distances.append(int(distance))
        return distances

    def get_distance(self, v1, v2):
        lca = self.get_lca(v1, v2)
        distance = self.weights[v1] + self.weights[v2] - 2*self.weights[lca]
        return distance

    def get_lca(self, v1, v2):
        v1, v2 = (v1, v2) if self.levels[v1] > self.levels[v2] else (v2, v1)
        level_gap = self.levels[v1] - self.levels[v2]
        v1 = self.lift(v1, level_gap)
        # when level is the same and nodes are same => they are in the same sub stree
        if v1 == v2:
            return v1
        for exponent in range(self.max_exponent -1, -1, -1):
            if self.ancestors[v1][exponent] != -1 and self.ancestors[v1][exponent] != self.ancestors[v2][exponent]:
                v1 = self.ancestors[v1][exponent]
                v2 = self.ancestors[v2][exponent]
        return self.ancestors[v1][0]
        # LCA might not be 2^n it can be 3 above from both node??

    def lift(self, node, k):
        binary = bin(k)[2:]
        for i, bit in enumerate(binary):
            if bit == "1":
                exponent = len(binary) - i - 1
                node = self.ancestors[node][exponent]
                if node == -1:
                    return -1
        return node


    def init_binary_lifting(self, n):
        self.max_exponent = ceil(math.log(n, 2)) + 1
        self.ancestors = [[
            -1 for i in range(self.max_exponent)]
            for j in range(self.n)]
        self.levels = {}
        self.weights = {}
        self.dfs(0)
        for exponent in range(self.max_exponent):
            self.ancestors[0][exponent] = -1
        for exponent in range(1, self.max_exponent):
            for node in range(1, n):
                prev = self.ancestors[node][exponent-1]
                if prev != -1:
                    self.ancestors[node][exponent] = self.ancestors[prev][exponent-1]
        return self.levels, self.weights, self.ancestors
    

    def dfs(self, node, parent=-1, level=0, weight=0):
        self.levels[node] = level
        self.weights[node] = weight
        self.ancestors[node][0] = parent
        for ad, next_weight in self.ad_list[node]:
            if ad == parent:
                continue
            self.dfs(ad, node, level + 1, weight + next_weight)

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2, weight in edges:
            ad_list[v1].add((v2, weight))
            ad_list[v2].add((v1, weight))
        return ad_list
        