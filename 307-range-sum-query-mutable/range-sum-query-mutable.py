class SegmentTree:
    def __init__(self):
        self.sum = 0
        self.left = None
        self.right = None

    def build(self, nums, i, j):
        self.range = [i, j]
        if i == j:
            self.sum = nums[i]
            return self
        if i > j:
            return None
        m = (i + j) // 2
        self.left = SegmentTree().build(nums, i, m)
        self.right = SegmentTree().build(nums, m+1, j)
        self.sum += self.left.sum if self.left else 0
        self.sum += self.right.sum if self.right else 0
        return self

    def update(self, i, val):
        if i == self.range[0] and i == self.range[1]:
            gap = self.sum - val
            self.sum = val
            return gap
        if self.right and self.right.range[0] <= i and i <= self.right.range[1]:
            gap = self.right.update(i, val)
        else:
            gap = self.left.update(i, val)
        self.sum -= gap
        return gap

    def sumRange(self, i, j):
        if i == self.range[0] and j == self.range[1]:
            return self.sum
        if self.left and self.left.range[0] <= i and j <= self.left.range[1]:
            return self.left.sumRange(i, j)
        elif self.right and self.right.range[0] <= i and j <= self.right.range[1]:
            return self.right.sumRange(i, j)
        else:
            left_j = self.left.range[1]
            right_i = self.right.range[0]
            return self.left.sumRange(i, left_j) + self.right.sumRange(right_i, j)
             

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = SegmentTree()
        self.root.build(nums, 0, len(nums) - 1)
        #print(self.root.sum)
        

    def update(self, index: int, val: int) -> None:
        self.root.update(index, val)
        return
        

    def sumRange(self, left: int, right: int) -> int:
        return self.root.sumRange(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)