class Solution:
    # init ad_list
    # collected <= n - 2
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ad_list = self.init_ad_list(n, edges)
        collected = set()
        one_incomings = self.get_one_incomings(self.ad_list)
        while one_incomings and len(collected) < n - 2:
            count = len(one_incomings)
            for i in range(count):
                node = one_incomings.popleft()
                if node in collected:
                    continue
                collected.add(node)
                for ad in self.ad_list[node]:
                    self.ad_list[ad].remove(node)
                    if len(self.ad_list[ad]) == 1:
                        one_incomings.append(ad)
        return list(one_incomings)

    def get_one_incomings(self, ad_list):
        one_incomings = collections.deque()
        for node in ad_list.keys():
            if len(ad_list[node]) <= 1:
                one_incomings.append(node)
        return one_incomings


    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list

