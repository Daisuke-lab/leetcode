class Solution:
    def maxProduct(self, A: List[int], K: int, limit: int) -> int:
        N = len(A)

        @cache
        def dp(i, sign, altsum, prod, taken):
            if i == N:
                if altsum == K and taken and prod <= limit:
                    return prod
                return -1

            return max(
                dp(i + 1, sign, altsum, prod, taken),
                dp(i + 1, sign * -1, altsum + sign * A[i], min(limit + 1, prod * A[i]), 1),
            )

        ans = dp(0, 1, 0, 1, 0)
        dp.cache_clear()
        return ans