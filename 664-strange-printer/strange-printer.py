class Solution:
    def strangePrinter(self, s: str) -> int:
        self.memo = [[
            -1 for j in range(len(s))]
            for i in range(len(s))]
        self.s = s
        return self.dp(0, len(s) - 1)
        
    def dp(self, l, r):
        if l == r:
            return 1
        if self.memo[l][r] != -1:
            return self.memo[l][r]

        min_cost = float("inf")
        if self.s[l] == self.s[r]:
            min_cost = self.dp(l+1, r)
        else:
            for k in range(l, r):
                cost = self.dp(l, k) + self.dp(k+1, r)
                min_cost = min(min_cost, cost)
        self.memo[l][r] = min_cost
        return min_cost
            
            
                