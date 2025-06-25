class Solution:
    # is_alice
    # i
    # m
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        self.memo = [[[
            -1 for a in range(101)]
            for b in range(len(self.piles))]
            for c in range(2)]
        return self.dp(True, 0, 1)

    def dp(self, is_alice, i, m):
        if i >= len(self.piles):
            return 0
        if self.memo[is_alice][i][m] != -1:
            return self.memo[is_alice][i][m]
        start = 1
        end = 2*m
        profit = - float("inf") if is_alice else float("inf")
        curr_profit = 0
        for x in range(start, end+1):
            if i + x - 1 >= len(self.piles):
                break
            if is_alice:
                curr_profit += self.piles[i+x-1]
                total_profit = curr_profit + self.dp(False, i+x, max(x, m))
                profit = max(profit, total_profit)
            else:
                total_profit = self.dp(True, i+x, max(x, m))
                profit = min(profit, total_profit)
        self.memo[is_alice][i][m] = profit
        return profit