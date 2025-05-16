class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        ad_list = self.init_ad_list(n, edges)
        leaves = self.get_leaves(ad_list)
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                n -= 1
                leaf = leaves.popleft()
                for ad in ad_list[leaf]:
                    ad_list[ad].remove(leaf)
                    if len(ad_list[ad]) == 1:
                        leaves.append(ad)
        
        

    def get_leaves(self, ad_list):
        leaves = collections.deque()
        for node in ad_list.keys():
            if len(ad_list[node]) == 1:
                leaves.append(node)
        return leaves
    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list