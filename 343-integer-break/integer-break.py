class Solution:
    def integerBreak(self, n: int) -> int:
        self.memo = [-1 for i in range(n + 1)]
        self.n = n
        return self.dp(n)

    def dp(self, n):
        if n == 1:
            return 1
        elif self.memo[n] != -1:
            return self.memo[n]
        max_product = n if n != self.n else 0
        for i in range(1, n):
            product = i * self.dp(n - i)
            max_product = max(max_product, product)
        self.memo[n] = max_product
        return max_product
        