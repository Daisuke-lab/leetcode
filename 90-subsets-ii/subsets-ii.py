class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # to avoid duplicates, you want to sort first
        # case1: you don't include current
        # case2: you include current
        # since the output is the list of list, I use top down
        # if i == len(nums), stop and add it to the answer
        
        self.answer = []
        self.nums = sorted(nums)
        self.recursion(0, [])
        return self.answer

    def recursion(self, i, curr):
        if i == len(self.nums):
            self.answer.append(curr.copy())
            return
        curr.append(self.nums[i])
        self.recursion(i+1, curr)
        curr.pop()
        #curr_i = i
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i+1]:
            i += 1
        i += 1
        self.recursion(i, curr)

        