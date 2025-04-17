class Solution:
    # 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ad_list = self.init_ad_list(n, flights)
        dj_map = [float("inf") for i in range(n)]
        dj_map[src] = 0
        for i in range(k+1):
            new_dj_map = dj_map.copy()
            for node in range(n):
                if dj_map[node] == float("inf"):
                    continue
                spent = dj_map[node]
                for ad, price in ad_list[node]:
                    if new_dj_map[ad] > spent + price:
                        new_dj_map[ad] = spent + price
            dj_map = new_dj_map
            #print(dj_map)           
        
        
        return dj_map[dst] if dj_map[dst] != float("inf") else - 1

        

        
        

    def init_ad_list(self, n, flights):
        ad_list = [set() for i in range(n)]
        for src, dest, price in flights:
            ad_list[src].add((dest, price))
        return ad_list      