class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        self.n = len(nums)
        self.quick_select(nums, 0, len(nums) - 1)
        #print(nums)
        # if you simply swap it, at max, you have 2 mistakes
        # take it one and concat to the bottom
        self.wiggle(nums)
        #self.adjust(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
    def index(self, i):
            return (1 + 2 * i) % (self.n | 1)
    def wiggle(self, nums):
        i = j = 0
        k = self.n - 1
        mid = nums[self.n // 2]
        #print(mid)
        while j <= k:
            if nums[self.index(j)] > mid:
                nums[self.index(i)], nums[self.index(j)] = nums[self.index(j)], nums[self.index(i)]
                i += 1
                j += 1
            elif nums[self.index(j)] < mid:
                nums[self.index(j)], nums[self.index(k)] = nums[self.index(k)], nums[self.index(j)]
                k -= 1
            else:
                j += 1

                

    def quick_select(self,  nums, i, j):
        if i >= j:
            return
        pivot_index = self.get_pivot(nums, i, j)
        pivot_num = nums[pivot_index]
        nums[pivot_index] = nums[j]
        nums[j] = pivot_num
        left = i
        right = j - 1
        while left <= right:
            while left <= right and nums[left] < pivot_num:
                left += 1
                continue
            while left <= right and nums[right] > pivot_num:
                right -= 1
                continue
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        nums[j] = nums[left]
        nums[left] = pivot_num

        if left== len(nums) // 2:
            return
        if left > len(nums) // 2:
            self.quick_select(nums, i, left-1)
        else:
            self.quick_select(nums, left + 1, j)
        
        


    def get_pivot(self, nums, i, j):
        count = 0
        max_num_index = None
        second_max_num_index = None
        chosen = set()
        while count < 3:
            x = randint(i, j)
            if x is chosen:
                continue
            count += 1
            chosen.add(x)
            if max_num_index is None or nums[x] > nums[max_num_index]:
                second_max_num_index = max_num_index
                max_num_index = x
            elif second_max_num_index is None or nums[x] > nums[second_max_num_index]:
                second_max_num_index = x
        return second_max_num_index
                