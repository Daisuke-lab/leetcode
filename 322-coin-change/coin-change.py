class Solution:
    # (amount) = count
     
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.memo = {}
        return self.dp(amount)

    def dp(self, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.memo:
            return self.memo[amount]
        count = float("inf")
        for coin in self.coins:
            child_count = self.dp(amount - coin)
            if child_count != -1:
                count = min(count, child_count + 1)
        count = count if count != float("inf") else -1
        self.memo[amount] = count
        return count
        