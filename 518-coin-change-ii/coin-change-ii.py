class Solution:
    # amount: count
    # 
    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        self.memo = {}
        return self.dp(0, amount)

    def dp(self, i, amount):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if i == len(self.coins):
            return 0
        if (i, amount) in self.memo:
            return self.memo[(i, amount)]
        count = self.dp(i, amount-self.coins[i])
        count += self.dp(i+1, amount)
        self.memo[(i, amount)] = count
        return count
                