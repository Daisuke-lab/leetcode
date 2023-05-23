class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.recursion(nums)


    def recursion(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        else:
            left_sum = self.recursion(nums[:-1])
            right_sum = self.recursion(nums[1:])
            whole_sum = sum(nums)
            return max(left_sum, right_sum, whole_sum)
