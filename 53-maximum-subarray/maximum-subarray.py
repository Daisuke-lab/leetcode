class Solution:
    # you want to start from positive number for sure
    # you want to finish with positive number for sure
    # you have two options
    # case1: include current as subarray
    # case2: stop sub array
    # DP
    #
    def maxSubArray(self, nums: List[int]) -> int:
        tab = [0 for i in range(len(nums))]
        max_point = nums[0]
        for i in range(len(nums)):
            if i == 0:
                tab[0] = nums[0]
            else:
                if tab[i-1] > 0:
                    tab[i] = tab[i-1] + nums[i]
                else:
                    tab[i] = nums[i]
                max_point = max(tab[i], max_point)
        return max_point