class SegmentTree:
    def __init__(self):
        self.sum = 0
        self.range = []
        self.left = None
        self.right = None

    def build(self, nums, i, j):
        self.range = [i, j]
        if i == j:
            self.sum = nums[i]
            return 
        m = (i + j) // 2
        if i <= m:
            self.left = SegmentTree()
            self.left.build(nums, i, m)
            self.sum += self.left.sum
        if m + 1<= j:
            self.right = SegmentTree()
            self.right.build(nums, m+1, j)
            self.sum += self.right.sum
            

    def sumRange(self, i, j):
        if self.range[0] == i and self.range[1] == j:
           return self.sum
        # this is confirmed, because the range is definitely in the list
        elif self.left.range[0] <= i and j <= self.left.range[1]:
            return self.left.sumRange(i, j)
        elif self.right.range[0] <= i and j <= self.right.range[1]:
            return self.right.sumRange(i, j)
        else:
            left_i = i
            left_j = self.left.range[1]
            right_i = self.right.range[0]
            right_j = j
            return self.left.sumRange(left_i, left_j) + self.right.sumRange(right_i, right_j)

    def update(self, i, val):
        if self.range[0] == i and self.range[1] == i:
            gap = val - self.sum
            self.sum = val
            return gap
        elif self.left.range[0] <= i and i <= self.left.range[1]:
            gap = self.left.update(i, val)
        elif self.right.range[0] <= i and i <= self.right.range[1]:
            gap = self.right.update(i, val)
        self.sum += gap
        return gap
            


class NumArray:

    def __init__(self, nums: List[int]):
        self.root = SegmentTree()
        self.root.build(nums, 0, len(nums) - 1)
        

    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
        return
        

    def sumRange(self, left: int, right: int) -> int:
        return self.root.sumRange(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)