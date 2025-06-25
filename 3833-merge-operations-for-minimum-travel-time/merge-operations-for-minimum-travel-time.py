class Solution:
    # if i - j are merged, you don't know which speed you should use
    # => It depends on how much you merge so far.
    # => That is not True. regardless of how many times you merge, it doesn't affect index
    # if you merge => you use sum of time as speed
    # if you don't merge => you use individual time as speed

    # When you merge, where is happening to combine time
    def minTravelTime(self, l: int, n: int, k: int, positions: List[int], times: List[int]) -> int:
        self.prefix_sums = self.get_prefix_sums(times)
        self.positions = positions
        self.times = times
        self.n = n
        self.memo = [[[
            -1 for p in range(k+1)]
                for j in range(n)]
                for i in range(n)]
        return self.dp(0, 0, k, times[0])
    
    def dp(self, i, j, k, speed):
        #print(i, j, k)
        if j == len(self.positions) -1:
            if k == 0:
                return 0
            else:
                return float("inf")
        if self.memo[i][j][k] != -1:
            return self.memo[i][j][k]


        min_cost = float("inf")
        original_k = k
        next_speed = 0
        next_i = j + 1
        # because you seperate merge, 0,3, you don't nerge 3, 8. that will be (i, j) = 0, 2
        for next_j in range(j+1, self.n):
            if k < 0:
                break
            distance = self.positions[next_j] - self.positions[j]
            next_speed += self.times[next_j]
            # In the first iteration, it'd be self.dp(j+1, j+1, k) => when you don't merge i to j
            cost = distance * speed + self.dp(next_i, next_j, k, next_speed)
            min_cost = min(min_cost, cost)
            k-= 1
        k = original_k
        self.memo[i][j][k] = min_cost
        return min_cost

        

        
        



    
    def get_prefix_sums(self, nums):
        prefix_sums = []
        for num in nums:
            if prefix_sums:
                prefix_sums.append(num + prefix_sums[-1])
            else:
                prefix_sums.append(num)
        return prefix_sums