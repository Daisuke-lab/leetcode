class Solution:
    # how do you define k
    
    ## Brute Force
    # 1. decide gap O(n^2)
    # 2. loop until you find current + gap number: O(n)
    # O(n^3)

    # flankly O(n) is impossible. let's make it O(n^2)
    # Count gap => [20, 17, 43, 45] 25:2 
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        longest = 2
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                longest = max(longest, dp[i][diff])

        return longest