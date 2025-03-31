class Solution:
    # get sum first.
    # if it's odd return false
    
    # Brute Force
    # you have two choices at every element. You choose the element or not
    # Time complexity is O(2^n)
    
    # Is sort helpful ??
    # this is actually combination sum question
    # reduce target by selecting num, and also remove selected num 
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2:
            return False
        target = num_sum // 2
        self.memo = {}
        self.nums = nums
        return self.dp(0, target)

    def dp(self, i, target):
        key = (i, target)
        if target == 0:
            return True
        elif i == len(self.nums):
            return False
        elif target < 0:
            return False
        elif key in self.memo:
            return self.memo[key]
        else:
            result = self.dp(i+1, target - self.nums[i])
            result = self.dp(i+1, target) or result
            self.memo[key] = result
            return result

        