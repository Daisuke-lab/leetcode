class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.ad_list = self.init_ad_list(n, flights)
        bf_map = [float("inf") for i in range(n)]
        bf_map[src] = 0
        for _k in range(k + 1):
            new_bf_map = bf_map.copy()
            for node in range(n):
                # when you haven't arrived node in _k time yet
                if bf_map[node] == float("inf"):
                    continue
                for price, ad in self.ad_list[node]:
                    if new_bf_map[ad] > bf_map[node] + price:
                        new_bf_map[ad] = bf_map[node] + price
            bf_map = new_bf_map
        return bf_map[dst] if bf_map[dst] != float("inf") else -1

    def init_ad_list(self, n, flights):
        ad_list = [set() for i in range(n)]
        for src, dest, price in flights:
            ad_list[src].add((price, dest))
        return ad_list      