class Solution:
    # every partition

    # you want to create the half of sum
    # knapscak
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        self.memo = {}
        self.nums = nums
        return self.dp(0, target)
        
    def dp(self, i, target):
        #print(i, target)
        if target == 0:
            return True
        elif target < 0:
            return False
        elif i == len(self.nums):
            return False
        elif (i, target) in self.memo:
            return self.memo[(i, target)]
        result = self.dp(i+1, target) or self.dp(i+1, target - self.nums[i])
        self.memo[(i, target)] = result
        return result