class Solution:
    # you can split stones to two sides
    # you want them to be nearly equal
    # find min remaining
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.stones = stones
        total_sum = sum(self.stones)
        target = total_sum // 2
        self.memo = [[
            -1 for i in range(target + 1)]
            for j in range(len(self.stones))]

        remain = self.dp(0, target)
        left = target - remain
        right = total_sum - left
        return abs(right - left)

    def dp(self, i, remain):
        if remain < 0:
            return float("inf")
        if i >= len(self.stones):
            return remain
        if self.memo[i][remain] != -1:
            return self.memo[i][remain]
        min_remain = remain
        min_remain = min(min_remain, self.dp(i+1, remain))
        min_remain = min(min_remain, self.dp(i+1, remain-self.stones[i]))
        self.memo[i][remain] = min_remain
        return min_remain
        