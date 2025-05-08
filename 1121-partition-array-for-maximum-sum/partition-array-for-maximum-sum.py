class Solution:
    # prefix sum 
    # l, r
    # 
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.k = k
        self.nums = arr
        self.memo = [-1 for i in range(len(self.nums))]
        return self.dp(0)

    def dp(self, i):
        if i >= len(self.nums):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        max_sum = 0
        max_num = self.nums[i]
        for j in range(self.k):
            if i + j >= len(self.nums):
                break
            max_num = max(max_num, self.nums[i + j])
            length = j + 1
            curr_sum = max_num * length
            curr_sum += self.dp(i+j+1)
            max_sum = max(max_sum, curr_sum)
        self.memo[i] = max_sum
        return max_sum
            