class Solution:
    # k = 0 => 1
    # k = 1 => 2, 3
    # k = 2 => 3
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = set()
        queue = collections.deque()
        queue.append(src)
        ad_list = self.init_ad_list(n, flights)
        prices = [float("inf") for i in range(n)]
        prices[src] = 0
        while k >= 0:
            count = len(queue)
            k -= 1
            next_prices = prices.copy()
            #print(queue)
            for i in range(count):
                node = queue.popleft()
                for ad, flight_price in ad_list[node]:
                    if prices[node] + flight_price < next_prices[ad]:
                        next_prices[ad] = prices[node] + flight_price
                        queue.append(ad)
            prices = next_prices
        return prices[dst] if prices[dst] != float("inf") else -1 

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2, price in edges:
            ad_list[v1].add((v2, price))
        return ad_list