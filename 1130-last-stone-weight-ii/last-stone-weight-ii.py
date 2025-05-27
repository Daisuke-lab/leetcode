class Solution:
    # Brute Force
    # n(n-1) + (n-1)(n-2) + .... => O(n^3)
    
    # how do you split the list
    # the base case: 1 or 2
    # choose the last stone to break
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.memo = {}
        self.stones = stones
        return self.dp(0, 0)
    def dp(self, i, total):
        if i == len(self.stones):
            return total
        elif (i, total) in self.memo:
            return self.memo[(i, total)]
        smallest_weight = float("inf")
        smallest_weight = min(smallest_weight, self.dp(i+1, total + self.stones[i]))
        smallest_weight = min(smallest_weight, self.dp(i+1, abs(total - self.stones[i])))
        self.memo[(i, total)] = smallest_weight
        return smallest_weight