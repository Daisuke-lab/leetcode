class Solution:
    # sorted => one way
    # unkonwn => two way
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.bs(0, len(nums) -1, False)

    def bs(self, l, r, figured):
        if l > r:
            return -1
        m = (l + r) //2
        result = -1
        if self.nums[m] == self.target:
            return m
        if figured:
            if self.nums[m] < self.target:
                return self.bs(m + 1, r, True)
            else:
                return self.bs(l, m -1, True)
        else:
            if self.nums[m] > self.nums[r]:
                result = self.bs(m+1, r, False)
            else:
                result = self.bs(m+1, r, True)
            if self.nums[l] > self.nums[r]:
                result = self.bs(l, m -1, False) if result == -1 else result
            else:
                result = self.bs(l, m -1, True) if result == -1 else result
        return result
            