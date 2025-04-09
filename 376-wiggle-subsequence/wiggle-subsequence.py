class Solution:
    # DP?? 
    # but you want to know the last is positive or negative
    # If you have two numbers, it definity two
    # 
    def wiggleMaxLength(self, nums: List[int]) -> int:
        tab = [[1,1] for i in range(len(nums))]
        max_length = 1
        for i in range(len(nums) -1, -1, -1):
            j = i + 1
            while j < len(nums):
                # Positive
                if nums[i] < nums[j]:
                    tab[i][0] = max(tab[i][0], tab[j][1]+1)
                elif nums[i] > nums[j]:
                    tab[i][1] = max(tab[i][1], tab[j][0] + 1)
                j += 1
            max_length = max(max_length, max(tab[i]))
        return max_length