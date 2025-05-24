class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # since the output is list of list, it is top to bottom
        # you want to keep answer as insntace variable
        # you maintain the list of added numbers so far
        # you also need to pass indexes of added number not to add the same number twice
        # stop it is equal to len(nums)
        # since all nums are unique, memoization is useless
        # O(n! * n) => n!: the number of recursion, n: for loop
        self.answer = []
        self.nums = nums
        self.all_visited = (1 << len(self.nums)) - 1
        self.recursion([], 0)
        return self.answer

    def recursion(self, curr, visited):
        if len(curr) == len(self.nums):
            self.answer.append(curr.copy())
            return
        for i, num in enumerate(self.nums):
            unvisited = (1 << i) & visited == 0
            if unvisited:
                curr.append(num)
                new_visited = (1 << i) | visited
                self.recursion(curr, new_visited)
                curr.pop()