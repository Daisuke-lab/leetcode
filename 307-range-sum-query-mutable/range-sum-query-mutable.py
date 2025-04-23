class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.trees = [0] * self.n + nums
        for i in range(self.n -1, 0, -1):
            self.trees[i]= self.trees[i*2] + self.trees[i*2+1]
        #print(self.trees)
    
    def update(self, i, val):
        i += self.n
        diff = val - self.trees[i]
        self.trees[i] = val
        i //= 2
        while i > 0:
            self.trees[i] += diff
            i //= 2
    
    def sumRange(self, i, j):
        i += self.n
        j += self.n
        answer = 0
        while i <= j:
            if i % 2 == 1:
                answer += self.trees[i]
                i += 1
            if j % 2 == 0:
                answer += self.trees[j]
                j -= 1
            i //= 2
            j //= 2
        return answer
        
             

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = SegmentTree(nums)
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