class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.sums = [0 for i in range(self.n*2)]
        for i in range(len(self.sums) -1, 0, -1):
            j = (i - self.n)
            if j >= 0:
                self.sums[i] = nums[j]
            else:
                left = i * 2
                right = i * 2 + 1
                self.sums[i] += self.sums[left]
                self.sums[i] += self.sums[right]
        #print(self.sums)
    
    def update(self, num, i):
        i = self.n + i
        gap = num - self.sums[i]
        while i > 0:
            self.sums[i] += gap
            i = i // 2
        
    def get_sum_range(self, i, j):
        curr_sum = 0
        i += self.n
        j += self.n
        # for i, if it is on the left side, sum will be included in parent
        # for j, if it is on the right side, sum will be included in parent
        
        while i <= j:
            # right side
            if i % 2 == 1:
                curr_sum += self.sums[i]
                i += 1
            # left side
            if j % 2 == 0:
                curr_sum += self.sums[j]
                j -= 1
            i = i // 2
            j = j // 2
        return curr_sum

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)


    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(val, index)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.get_sum_range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)