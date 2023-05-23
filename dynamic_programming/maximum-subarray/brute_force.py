class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.brute_force(nums)

    def brute_force(self, nums):
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                temp = sum(nums[i:j])
                if max_sum < temp:
                    max_sum = temp


        return max_sum