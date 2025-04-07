class Solution:
    # you want to start from positive number for sure
    # you want to finish with positive number for sure
    # you have two options
    # case1: include current as subarray
    # case2: stop sub array
    # DP
    #
    def maxSubArray(self, nums: List[int]) -> int:
        tab = [0, 0]
        max_point = nums[0]
        for i in range(len(nums)):
            if i == 0:
                tab[1] = nums[i]
            else:
                if tab[1] > 0:
                    tab_num = tab[1] + nums[i]
                else:
                    tab_num = nums[i]
                tab[0] = tab[1]
                tab[1] = tab_num
                max_point = max(tab[1], max_point)
        return max_point