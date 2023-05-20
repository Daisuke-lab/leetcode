class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.recursion(nums, 0)


    def recursion_with_memo(self, nums, i):
        return

    def recursion(self, nums, i):
        if i == len(nums) - 1:
            return 0
        elif i >= len(nums):
            return float("inf")

        else:
            steps = nums[i]
            count = 0
            min_count = float("inf")
            for step in range(1, steps+1):
               count = self.recursion(nums, i + step)
               if min_count > count:
                   min_count = count
            
            return min_count + 1