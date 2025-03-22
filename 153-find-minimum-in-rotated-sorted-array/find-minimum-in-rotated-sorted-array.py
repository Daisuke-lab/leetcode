class Solution:
    def findMin(self, nums: List[int]) -> int:
        # This is not fully efficient because even when left and right side are sorted, it keeps searching left side
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            # If right side is sorted. the answer is always left side in spite of that left is sorted or owns pivot 
            if nums[m] < nums[r]:
                r = m
            # It right side is not sorted, it means right side has pivot.
            else:
                l = m + 1
        return nums[l]


        