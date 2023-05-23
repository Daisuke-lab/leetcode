class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.recursion_with_memo(nums, {})


    def recursion_with_memo(self, nums, memo):
        key = str(nums)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        elif key in memo:
            return memo[key]
        else:
            left_sum = self.recursion_with_memo(nums[:-1], memo)
            right_sum = self.recursion_with_memo(nums[1:], memo)
            whole_sum = sum(nums)
            memo[key] = max(left_sum, right_sum, whole_sum)
            return memo[key]