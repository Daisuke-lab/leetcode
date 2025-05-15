class Solution:
    # Brute Force
    # try with perfect squares 1, 4, 9, 
    # you have 2 chioices. whether you include 1 or not

    # it's like a combination sum 
    # so, curr and n
    # but n is too huge
    # hashmap
    def numSquares(self, n: int) -> int:
        self.memo = {}
        curr = int(math.sqrt(n))
        return self.dp(n)


    def dp(self, n):
        if n == 0:
            return 0
        if n < 0:
            return float("inf")
        if n in self.memo:
            return self.memo[n]
        min_cost = float("inf") 
        for digit in range(int(math.sqrt(n)), 0, -1):
            square = digit ** 2
            min_cost = min(min_cost, self.dp(n - square) + 1)
        self.memo[n] = min_cost
        return min_cost