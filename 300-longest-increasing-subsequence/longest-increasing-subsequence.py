class Solution:
    # every time you have 2 choices either you include current value or not => 2^n
    # you want to use DP
    # how can you cache it??
    # tab [max_length] => n^2
    # how about top down
    # you also have a chance to start subseqeuence at any position => O(n)

    def lengthOfLIS(self, nums: List[int]) -> int:
        tab = [1 for i in range(len(nums))]
        for i in range(len(nums) -1 , -1, -1):
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    tab[i] = max(tab[i], tab[j]+1)
                j += 1
        return max(tab)
            
        