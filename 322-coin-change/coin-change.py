class Solution:
    # You can use coins as many times as you want
    # The first idea is to reduce amoount and pass the same coins
    # Because you want to minimize the coins, you can reverse sort
    # the first answer you find is the right answer. You don't need even cache
    # But when you cannot find combination, you want to stop iteration as fast as possible
    # To do that, you need to know minimum count and amount, so you can not set count as global variable
    # 
    # As Global variable
    # self.coins
    # self.memo
    # As Function 
    # dp(amount): => return count:integer
    # if amount == 0, return 0
    # if amount < 0, return -1
    # if amount > 0,
    # => loop child
    # => if child's answer >= 0, choose minimum
    # add 1 to minimum
    # save it to the memo
    # return count
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = sorted(coins, reverse=True)

        self.memo = {}
        return self.dp(amount)


    def dp(self, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        elif amount in self.memo:
            return self.memo[amount]
        count = -1
        for coin in self.coins:
            child_count = self.dp(amount - coin)
            if count == -1 and child_count != -1:
                count = child_count
            elif child_count != -1:
                count = min(count, child_count)
        if count != -1:
            count += 1
        self.memo[amount] = count
        return count
        