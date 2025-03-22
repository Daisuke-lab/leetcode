class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        self.nums = nums
        while l <= r:
            m = (l + r) // 2
            if m == l and m == r:
                return nums[m]
            elif self.in_left_sorted(l, m) and not self.in_right_sorted(m, r):
                l = m + 1
            elif not self.in_left_sorted(l, m) and self.in_right_sorted(m, r):
                r = m
            else:
                return nums[l]


    def in_left_sorted(self, l, m):
        return self.nums[l] <= self.nums[m]
    def in_right_sorted(self, m, r):
        return self.nums[m] <= self.nums[r]
        
        