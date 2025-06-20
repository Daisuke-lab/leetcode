class Solution:
    # you have 3 choices
    # buy: 
    # sell: once you sell, i + 2
    # cooldown
    
    # args: i,j *i: where you buy, j: current
    # output: max_profit
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[
            0 for i in range(2)]
            for j in range(len(prices)+2)]
        for i in range(len(prices) -1, -1, -1):
            for has_stock in range(2):
                result = 0
                # when you don't have stock
                if has_stock == False:
                    # buy now
                    result = max(result, memo[i+1][True] - prices[i])
                    # don't buy
                    result = max(result, memo[i+1][False])
                else:
                    # sell now
                    result = max(result, memo[i+2][False] + prices[i])
                    # don't sell
                    result = max(result, memo[i+1][True])
                memo[i][has_stock] = result
        return memo[0][False]

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