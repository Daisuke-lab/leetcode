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
        tab = [0] * 26
        max_length = 0
        for c in s:
            i = ord(c) - ord("a")
            range_start = max(0, i - k)
            range_end = min(26, i + k + 1)
            ad_max = max(tab[range_start:range_end])
            tab[i] = 1 + ad_max
            max_length = max(tab[i], max_length)
        return max_length
        