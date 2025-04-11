class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        target = len(nums)//2 + 1
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                count += 1
                if target == count:
                    return nums[i]
            else:
                count = 1
        return nums[-1]
        
        