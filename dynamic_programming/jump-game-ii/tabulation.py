class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.tabulation(nums)

    def tabulation(self, nums):
        tabs = [float("inf") for num in nums]
        tabs[0] = 0
        for i in range(len(nums)):
            steps = nums[i]
            if tabs[i] != float("inf"):
                for step in range(1, steps+1):
                    min_count = tabs[i] + 1
                    if len(tabs) > i + step and tabs[i + step] > min_count:
                        tabs[i + step] = min_count