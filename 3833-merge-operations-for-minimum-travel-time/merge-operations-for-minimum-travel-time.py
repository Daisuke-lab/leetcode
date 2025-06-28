class Solution:
    # if i - j are merged, you don't know which speed you should use
    # => It depends on how much you merge so far.
    # => That is not True. regardless of how many times you merge, it doesn't affect index
    # if you merge => you use sum of time as speed
    # if you don't merge => you use individual time as speed

    # 
    def minTravelTime(self, l: int, n: int, k: int, positions: List[int], times: List[int]) -> int:
        self.positions = positions
        self.times = times
        self.n = n
        self.memo = [[[
            -1 for a in range(101)]
            for p in range(k+1)]
                for i in range(n)]
        result = self.dp(0, k, times[0])
        return result
    
    def dp(self, i, k, speed):
        if i >= len(self.positions)-1:
            if k == 0:
                return 0
            else:
                return float("inf")
        #print(i, k, speed)
        if self.memo[i][k][speed] != -1:
            return self.memo[i][k][speed]


        min_cost = float("inf")
        original_k = k
        next_speed = 0
        for j in range(i+1, self.n):
            if k < 0:
                break
            distance = self.positions[j] - self.positions[i]
            next_speed += self.times[j]
            # In the first iteration, it'd be self.dp(j+1, j+1, k) => when you don't merge i to j
            cost = distance * speed + self.dp(j, k, next_speed)
            min_cost = min(min_cost, cost)
            k-= 1
        k = original_k
        self.memo[i][k][speed] = min_cost
        return min_cost