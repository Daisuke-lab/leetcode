class Solution:
    # Good test case: # 13313

    # Brute Force
    # sort it 
    # divide into 2
    # merge it 
    # O(nlogn)

    # Bucket Sort
    # sort it num_value as index, count as value
    # compress it
    # find the middle point
    # O(n)
    # But this is O(n) memory complexity
    
    # 2 pointers
    # greedy
    # quick select
    # binary search
    # 112233
    # 122133
    # 213123
    
    # find the middle point by quick select
    # partition i, j => i jumps with 2, j jumps with 1
    # what is the edge case? 112233, 11333, 11133 => It matters when you have odd numbers
    # 11313
    # solution 1: expand from middle => 1,2,3 is a counter example. 2 isn't center
    # 11223 => 12231
    # 2 => 121 => 21213
    # 12132
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        #self.quick_select(nums, 0, len(nums) - 1)
        nums.sort()
        # if you simply swap it, at max, you have 2 mistakes
        # take it one and concat to the bottom
        #self.wiggle(nums)
        #self.adjust(nums)
        mid = (len(nums) + 1) // 2
        left, right = nums[:mid][::-1], nums[mid:][::-1]
        nums[::2], nums[1::2] = left, right
        """
        Do not return anything, modify nums in-place instead.
        """

    def wiggle(self, nums):
        i = 1
        j = len(nums) -1
        while i <= j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 2
            j -= 2

    def adjust(self, nums):
        invalid = False
        invalid_num = None
        direction = "up" if nums[0] < nums[1] else "down"
        for i in range(len(nums)-1):
            if invalid:
                nums[i] = nums[i+1]
                continue
            if direction == "up" and nums[i] > nums[i+1]:
                invalid = True
                invalid_num = nums[i]
                nums[i] = nums[i+1]
            if direction == "down" and nums[i] < nums[i+1]:
                invalid = True
                invalid_num = nums[i]
                nums[i] = nums[i+1]
            direction = "up" if direction == "down" else "down"
        if invalid:
            nums[-1] = invalid_num
                

    def quick_select(self,  nums, i, j):
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

        if left == len(nums) // 2:
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
                