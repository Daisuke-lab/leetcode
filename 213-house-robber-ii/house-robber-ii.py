class Solution:
    def rob(self, nums: List[int]) -> int:
        # [steal from first house, don't steal from the first house]
        tab = [[0, 0] for i in range(len(nums))]
        tab[0][0] = nums[0]
        if len(nums) == 1:
            return tab[0][0]
        tab[1][1] = nums[1]
        tab[1][0] = nums[0]
        max_money = max(nums[0], nums[1])
        for i in range(2, len(tab)):
            tab[i][0] = max(tab[i-1][0], tab[i-2][0] + nums[i])
            tab[i][1] = max(tab[i-1][1], tab[i-2][1] + nums[i])
            if i == len(tab) -1:
                tab[i][0] = 0
            max_money = max(max_money, max(tab[i]))
        return max_money
        