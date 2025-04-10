class Solution:
    # where to start
    # n^2
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        tab = [1 for i in range(len(nums))]
        max_length = 1
        for i in range(len(nums)-1, -1, -1):
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    tab[i] = max(tab[i], tab[j]+1)
                j += 1
            max_length = max(max_length, tab[i])
            if max_length >= 3:
                return True
        return False
            