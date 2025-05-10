class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        self.nums = nums
        self.target = target
        return self.bs(0, len(nums) -1, False)

    def bs(self, l, r, figured):
        if l > r:
            return False
        m = (l + r) //2
        result = False
        if self.nums[m] == self.target:
            return True
        if figured:
            if self.nums[m] < self.target:
                return self.bs(m + 1, r, True)
            else:
                return self.bs(l, m -1, True)
        else:
            if self.nums[m] >= self.nums[r]:
                result = self.bs(m+1, r, False)
            else:
                result = self.bs(m+1, r, True)
            if self.nums[l] >= self.nums[m]:
                result = self.bs(l, m -1, False) or result
            else:
                result = self.bs(l, m -1, True) or result
        return result