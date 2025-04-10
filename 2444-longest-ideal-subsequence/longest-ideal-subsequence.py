class Solution:
    # you have two choices
    # case1: you drop i
    # case2: you drop i+1
    # case3: don't drop
    # O(n^3)

    # The target is O(n^2)
    # tab = i[], {: length}
    # what do you want??
    # I want length at j so far and I want to add 1 for i
    # O(n^2)
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            i = ord(ch) - ord("a")
            dp[i] = 1 + max(dp[max(0, i - k) : min(26, i + k + 1)])
        return max(dp)
        