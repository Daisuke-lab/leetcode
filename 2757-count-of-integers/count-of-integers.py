class Solution:
    # upper_tight: tight with num2
    # lower_tight: tight with num1
    # how do you get sum?? => you can carry curr 
    
    # args: i, upper_tight, lower_tight, curr
    # output: count

    # what is the inital value
    #  i=0, and both are tight, curr = 0
    
    # what is the base case
    # out of range=> make sure curr is bigger than min_sum
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        self.num1 = num1
        self.num2 = num2
        self.num1 = (len(self.num2) - len(self.num1)) * "0" + self.num1
        self.n = len(self.num1)
        self.min_sum = min_sum
        self.max_sum = max_sum
        self.memo = [[[[
            -1 for a in range(401)]
            for b in range(2)]
            for c in range(2)]
            for d in range(self.n)]
        return self.dp(0, True, True, 0)

    def dp(self, i, lower_tight, upper_tight, curr):
        if curr > self.max_sum:
            return 0
        if i >= self.n:
            if curr >= self.min_sum:
                return 1
            else:
                return 0
        if self.memo[i][lower_tight][upper_tight][curr] != -1:
            return self.memo[i][lower_tight][upper_tight][curr]
        start = int(self.num1[i]) if lower_tight else 0
        end = int(self.num2[i]) if upper_tight else 9
        count = 0
        for digit in range(start, end+1):
            next_lower_tight = lower_tight and digit == start
            next_upper_tight = upper_tight and digit == end
            count += self.dp(i+1, next_lower_tight, next_upper_tight, curr + digit)
        self.memo[i][lower_tight][upper_tight][curr] = count % (10**9 + 7)
        return self.memo[i][lower_tight][upper_tight][curr]
        
