class Solution:
    # you want to cut every pattern
    # l, r
    # too slow

    # l, r in cuts
    # length always the same based on l and r
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts = sorted(cuts)
        self.memo = [[
            -1 for j in range(len(cuts))]
            for i in range(len(cuts))]
        return self.dp(0, len(self.cuts) - 1, 0, n)
        
    def dp(self, l, r, start, end):
        if l < 0 or r >= len(self.cuts) or l > r:
            return 0
        if self.memo[l][r] != -1:
            return self.memo[l][r]

        min_cost = float("inf")
        for i in range(l, r + 1):
            cost = end - start
            cost += self.dp(l, i-1, start,  self.cuts[i])
            cost += self.dp(i + 1, r, self.cuts[i], end)
            min_cost = min(min_cost, cost)
        self.memo[l][r] = min_cost
        #print(start, end, min_cost)
        return min_cost