class Solution:
    def minTravelTime(self, l: int, n: int, k: int, positions: List[int], times: List[int]) -> int:
        self.time_prefix_sums = self.get_prefix_sums(times)
        self.positions = positions
        self.n = n
        self.memo = [[[
            -1 for p in range(k+1)]
                for j in range(n)]
                for i in range(n)]
        result = self.dp(0, 0, k)
        return result
        
    # the minimul travel time when i <=> j is already merged
    def dp(self, i, j, k):
        #print(i, j, k)
        if j == self.n -1:
            if k == 0:
                return 0
            else:
                return float("inf")
        if self.memo[i][j][k] != -1:
            return self.memo[i][j][k]
        # the speed when you merge from i to j
        # you would't change the spped at i when you merge, it changes at i + 1
        rate = self.time_prefix_sums[j] - self.time_prefix_sums[i-1] if i != 0 else self.time_prefix_sums[j]
        #print(rate)


        result = float("inf")
        original_k = k
        for next_j in range(j+1, self.n):
            if k < 0:
                break
            distance = self.positions[next_j] - self.positions[j]
            # In the first iteration, it'd be self.dp(j+1, j+1, k) => when you don't merge i to j
            cost = distance * rate + self.dp(j+1, next_j, k)
            result = min(result, cost)
            k-= 1
        k = original_k
        self.memo[i][j][k] = result
        return result

    def get_prefix_sums(self, nums):
        prefix_sums = []
        for num in nums:
            if len(prefix_sums) == 0:
                prefix_sums.append(num)
            else:
                prefix_sums.append(num + prefix_sums[-1])
        return prefix_sums