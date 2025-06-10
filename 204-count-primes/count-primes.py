class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        limit = ceil(math.sqrt(n))
        memo = [1 for i in range(n)]
        memo[0] = 0
        memo[1] = 0
        for i in range(limit):
            if memo[i] == 0:
                continue
            for j in range(i*2, n, i):
                memo[j] = 0
        return sum(memo)