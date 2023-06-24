class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.recursion(nums, 0, {})


    def recursion(self, nums, i):
        if i == len(nums) -1:
            return True
        if i > len(nums) -1:
            return False

        for j in range(1, nums[i]+1):
            if self.recursion(nums, i+j):
                return True

        return False