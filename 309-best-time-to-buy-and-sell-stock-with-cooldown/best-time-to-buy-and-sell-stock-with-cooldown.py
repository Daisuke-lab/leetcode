class Solution:
    # [holdingStock (price), i] = maxProfit
    # you can sell it but you don't know how to buy
    # 
    def maxProfit(self, prices: List[int]) -> int:
        self.memo = {}
        self.prices = prices
        return self.dp(0, False)

    def dp(self, i, has_stock):
        if i >= len(self.prices):
            return 0
        elif (i, has_stock) in self.memo:
            return self.memo[(i, has_stock)]
        
        profit = 0

        # SELL
        if has_stock:
            profit = max(profit, self.dp(i+2, False) + self.prices[i])
        # BUY
        else:
            profit = max(profit, self.dp(i+1, True) - self.prices[i])

        # if you don't do anything
        profit = max(profit, self.dp(i+1, has_stock))
        self.memo[(i, has_stock)] = profit
        return profit
        
        