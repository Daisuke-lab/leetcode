class Solution:
    # you have 3 choices
    # buy: 
    # sell: once you sell, i + 2
    # cooldown
    
    # args: i,j *i: where you buy, j: current
    # output: max_profit
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.memo = [[
            -1 for i in range(2)]
            for j in range(len(prices))]
        return self.dp(0, False)

    def dp(self, i, has_stock):
        if i >= len(self.prices):
            return 0
        if self.memo[i][has_stock] != -1:
            return self.memo[i][has_stock]
        result = 0
        # when you don't have stock
        if has_stock is False:
            # buy now
            result = max(result, self.dp(i+1, True) - self.prices[i])
            # don't buy
            result = max(result, self.dp(i+1, False))
        else:
            # sell now
            result = max(result, self.dp(i+2, False) + self.prices[i])
            # don't sell
            result = max(result, self.dp(i+1, True))
        self.memo[i][has_stock] = result
        return result