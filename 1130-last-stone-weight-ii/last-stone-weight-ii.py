class Solution:
    # Brute Force
    # n(n-1) + (n-1)(n-2) + .... => O(n^3)
    
    # how do you split the list
    # the base case: 1 or 2
    # choose the last stone to break
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.memo = {}
        self.stones = stones
        total_sum = sum(stones)
        target = total_sum // 2
        remaining = self.dp(0, target)
        if remaining == 0 and total_sum % 2 == 0:
            return 0
        else:
            left = target - remaining
            right = total_sum - left
            return abs(left - right)
    def dp(self, i, target):
        if target == 0:
            return 0
        elif target < 0:
            return float("inf")
        elif i == len(self.stones):
            return target
        elif (i, target) in self.memo:
            return self.memo[(i, target)]
        result = min(self.dp(i+1, target), self.dp(i+1, target-self.stones[i]))
        self.memo[(i, target)] = result
        return result