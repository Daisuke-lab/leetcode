class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        self.nums = nums
        while l <= r:
            m = (l + r) // 2
            if m == l and m == r:
                return nums[m]
            # It means right side has pivot, and min value is around pivot
            elif self.in_left_sorted(l, m) and not self.in_right_sorted(m, r):
                l = m + 1
            # It means left side has pivot, and min value is around pivot
            elif not self.in_left_sorted(l, m) and self.in_right_sorted(m, r):
                r = m
            # the portion of list is already sorted. you can return the most left value as min
            else:
                return nums[l]


    def in_left_sorted(self, l, m):
        return self.nums[l] <= self.nums[m]
    def in_right_sorted(self, m, r):
        return self.nums[m] <= self.nums[r]
        
        