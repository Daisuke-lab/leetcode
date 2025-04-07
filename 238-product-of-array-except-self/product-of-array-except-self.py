class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            prefixes.append(prefix)
            suffixes.insert(0, suffix)
            prefix *= nums[i]
            suffix *= nums[j]
        answer = []
        for i in range(len(nums)):
            answer.append(prefixes[i]*suffixes[i])
        return answer