class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tab = [num for num in nums]
        for i in range(1, len(nums)):
            tab[i] = max(tab[i-1] + nums[i], nums[i])
        return max(tab)