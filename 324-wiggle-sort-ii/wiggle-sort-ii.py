class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        self.n = len(nums)
        self.quick_select(nums, 0, len(nums) - 1)
        self.wiggle(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
    # 
    def index(self, i):
            return (1 + 2 * i) % (self.n | 1)
    def wiggle(self, nums):
        i = k = 0
        j = self.n - 1
        median = nums[self.n // 2]

        #print(mid)
        while k <= j:
            # if it is bigger than median, you insert from left side (odd index)
            if nums[self.index(k)] > median:
                nums[self.index(i)], nums[self.index(k)] = nums[self.index(k)], nums[self.index(i)]
                i += 1
                k += 1
            # if it is smaller than median, you insert from right side (even index)
            elif nums[self.index(k)] < median:
                nums[self.index(j)], nums[self.index(k)] = nums[self.index(k)], nums[self.index(j)]
                j -= 1
            # if self.index(k) equal to median, it is not inserted to anywhere
            # so the worse case, you have n/2 medians (e.g., [1,1,1,1,3,4,5])
            # forget about 1, think of 3,4,5. It foes to odd index 100% 
            # so it create [x,3,x,4,x,5,x]
            # One thing you should notice that self.index(k) == self.index(k-1) == median doesn't mean
            # you have consecutive median. It is actually index(k) = 1,3,5,0,2,4,6
            # Again, it is eventually going to be swapped by other if statements.
            # The bottom line is it's not going to be inserted into either left or right
            # But when you find smaller/bigger value than median, it is collected as left or right and swap the median value
            # to other half. 
            else:
                k += 1

                

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
                