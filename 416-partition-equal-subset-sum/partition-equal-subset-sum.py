class Solution:
    # target = half
    # knapsack
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        self.nums = nums
        # amount, i
        self.memo = [[
            -1 for i in range(len(nums))]
            for j in range(target + 1)]
        return self.dp(target, 0)

    def dp(self, amount, i):
        if amount == 0:
            return True
        if i >= len(self.nums):
            return False
        if amount < 0:
            return False
        if self.memo[amount][i] != -1:
            return self.memo[amount][i]
        result = False
        result = result or self.dp(amount - self.nums[i], i + 1)
        result = result or self.dp(amount, i + 1)
        self.memo[amount][i] = result
        return result