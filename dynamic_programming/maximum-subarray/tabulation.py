class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.tabulation(nums)


    def tabulation(self, nums):
        dp = [0]*len(nums)
        for i,num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)

