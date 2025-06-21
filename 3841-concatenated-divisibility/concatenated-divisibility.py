class Solution:
    # args: visited, reminder, curr
    # how do you get the list as output
    # you can pass it as arg but you don't have to cache
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        self.nums = sorted(nums)
        self.k = k
        self.all_visited = (1 << len(nums)) -1
        self.answer = []
        self.memo = [[
            -1 for a in range(k)]
            for b in range(self.all_visited + 1)]
        self.dp(0, 0, [])
        return self.answer
    def dp(self, visited, reminder, curr):
        if visited == self.all_visited and reminder == 0:
            self.answer = curr.copy()
        if len(self.answer) > 0:
            return
        if self.memo[visited][reminder] != -1:
            return 
        for i in range(len(self.nums)):
            unvisited = ((1 << i) & visited) == 0
            if unvisited:
                new_visited = (1 << i) | visited
                new_reminder = int(str(reminder) + str(self.nums[i])) % self.k 
                curr.append(self.nums[i])
                self.dp(new_visited, new_reminder, curr)
                del curr[-1]
        self.memo[visited][reminder] = 0
        