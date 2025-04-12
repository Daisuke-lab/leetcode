class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.mergeSort(0, len(nums) - 1)
        return nums

    def mergeSort(self, i, j):
        if i == j:
            return
        m = (i + j) //2
        self.mergeSort(i, m)
        self.mergeSort(m+1, j)
        left_nums = self.nums[i:m+1]
        right_nums = self.nums[m+1:j+1]
        #print(left_nums, right_nums)
        while left_nums or right_nums:
            if not left_nums:
                self.nums[i] = right_nums.pop(0)
            elif not right_nums:
                self.nums[i] = left_nums.pop(0)
            elif left_nums[0] < right_nums[0]:
                self.nums[i] = left_nums.pop(0)
            else:
                self.nums[i] = right_nums.pop(0)
            i += 1