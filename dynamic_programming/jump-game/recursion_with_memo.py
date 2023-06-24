class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recursion_with_memo(nums, 0, {})


    def recursion_with_memo(self, nums, i, memo):
        if i in memo:
            return memo[i]
        if i == len(nums) -1:
            memo[i] = True
            return True
        if i > len(nums) -1:
            memo[i] = False
            return False

        for j in range(1, nums[i]+1):
            if self.recursion_with_memo(nums, i+j, memo):
                memo[i] = True
                return True
        memo[i] = False
        return False