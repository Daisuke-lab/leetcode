class Solution:
    def strangePrinter(self, s: str) -> int:
        self.s = s
        self.memo = [[
            -1 for i in range(len(s))]
            for j in range(len(s))]
        return self.dp(0, len(s) -1 )

    def dp(self, i, j):
        if i > j:
            return 0
        elif i == j:
            return 1
        elif self.memo[i][j] != -1:
            return self.memo[i][j]
        elif self.s[i] == self.s[j]:
            self.memo[i][j] =  min(self.dp(i+1, j), self.dp(i, j-1))
            return self.memo[i][j]
        else:
            min_cost = float("inf")
            for k in range(i, j):
                cost = self.dp(i, k) + self.dp(k + 1, j)
                min_cost = min(min_cost, cost)
            self.memo[i][j] = min_cost
            return min_cost
