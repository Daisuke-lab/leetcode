class Solution:
    # you shold fix i, j
    # 
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums) -2):
                if j != i+1 and nums[j-1] == nums[j]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum == target:
                        answer.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l-1] == nums[l]:
                            l += 1
                    elif four_sum < target:
                        l += 1
                    else:
                        r -=1
        return answer