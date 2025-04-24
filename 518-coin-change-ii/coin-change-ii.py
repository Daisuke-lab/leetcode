class Solution:
    # amount: count
    # 
    def change(self, amount: int, coins: List[int]) -> int:
        grid = [[0 for j in range(len(coins))] for i in range(amount+1)]
        grid[0] = [1 for j in range(len(coins))]
        for i in range(1, amount+1):
            for j in range(len(coins)):
                coin = coins[j]
                count_when_curr_used = grid[i - coin][j] if i - coin >= 0 else 0
                count_when_curr_not_used = grid[i][j-1] if j - 1 >= 0 else 0
                grid[i][j] = count_when_curr_used +count_when_curr_not_used
        return grid[-1][-1]
                