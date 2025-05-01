import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.n = len(nums) // 2
        self.nums = nums
        self.all_visited = (1 << len(nums)) - 1
        self.memo = [[
            -1 for j in range(self.n+1)]
            for i in range(self.all_visited)]
        # print("ALL_VISITED:", bin(self.all_visited))
        # print("N:", self.n)
        return self.dp(0, 1)


    def dp(self, visited, operation):
        if visited == self.all_visited:
            return 0
        if operation > self.n:
            return 0
        # print("VISITED:", bin(visited))
        # print("OPERATION:", operation)
        if self.memo[visited][operation] != -1:
            return self.memo[visited][operation]
        max_score  = 0
        for i in range(len(self.nums) - 1):
            for j in range(i + 1, len(self.nums)):
                i_unvisited = (visited & (1 << i)) == 0
                j_unvisited = (visited & (1 << j)) == 0
                if i_unvisited and j_unvisited:
                    new_visited = visited | (1 << i) |(1 << j)
                    max_score = max(max_score, self.dp(new_visited, operation + 1) + math.gcd(self.nums[i], self.nums[j]) * operation)
        self.memo[visited][operation] = max_score
        return max_score