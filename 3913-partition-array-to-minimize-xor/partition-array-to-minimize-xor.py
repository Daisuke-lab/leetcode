class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Prefix XOR
        pfix = [0] * (n + 1)
        for i in range(1, n + 1):
            pfix[i] = pfix[i - 1] ^ nums[i - 1]

        # Step 2: DP table
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][1] = pfix[i]  # Base case: 1 partition

        # Step 3: Fill DP
        for parts in range(2, k + 1):
            for end in range(parts, n + 1):
                for split in range(parts - 1, end):
                    segmentXOR = pfix[end] ^ pfix[split]
                    maxXOR = max(dp[split][parts - 1], segmentXOR)
                    dp[end][parts] = min(dp[end][parts], maxXOR)

        return dp[n][k]