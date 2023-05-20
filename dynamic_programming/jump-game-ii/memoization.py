class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.recursion_with_memo(nums, 0, {})

    def recursion_with_memo(self, nums, i, memo):
        if i == len(nums) - 1:
            return 0
        elif i >= len(nums):
            return float("inf")
        elif memo.get(i) is not None:
            return memo.get(i)
        else:
            steps = nums[i]
            count = 0
            min_count = float("inf")
            for step in range(1, steps+1):
               count = self.recursion_with_memo(nums, i + step, memo)
               if min_count > count:
                   min_count = count
            memo[i] = min_count + 1
            return min_count + 1

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