class Solution:
    # visited, curr, 
    
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        self.k = k
        self.nums = nums
        self.all_visited = (1 << len(nums)) - 1
        self.power = [10**len(str(num)) % k for num in nums]
        self.indices = sorted(range(len(nums)), key=lambda i: nums[i])
        self.memo = [[
            -1 for i in range(k)]
            for j in range(self.all_visited)]
            
        result = self.dp(0, 0)
        return result if result is not None else []

    def dp(self, visited, rem):
        if self.all_visited == visited:
            return [] if rem == 0 else None
        if self.memo[visited][rem] != -1:
            return self.memo[visited][rem]
        result = None
        for i in self.indices:
            unvisited = (visited & (1 << i)) == 0
            if unvisited:
                new_visited = visited | (1 << i)
                new_rem = (rem * self.power[i] + self.nums[i]) % self.k
                result = self.dp(new_visited, new_rem)
                if result is not None:
                    result = [self.nums[i]] + result
                    break
        self.memo[visited][rem] = result
        return result   