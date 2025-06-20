class Solution:
    # args: tight, i
    # output: count

    # when you choose 1 now, you skip the index by 2
    
    # what is the base case?
    # when it's out of bound, you can return 1
    #
    def findIntegers(self, n: int) -> int:
        self.s = bin(n)[2:]
        self.n = len(self.s)
        self.memo = [[
            -1 for i in range(2)]
            for j in range(self.n)]
        return self.dp(0, True)

    def dp(self, i, tight):
        if i >= self.n:
            return 1
        if self.memo[i][tight] != -1:
            return self.memo[i][tight]
        limit = int(self.s[i]) if tight else 1
        count = 0
        for curr in range(limit + 1):
            next_tight = tight and curr == limit
            if curr == 1:
                next_tight = next_tight and self.s[i+1] == "0" if i + 1 < len(self.s) else False
                count += self.dp(i+2, next_tight)
            else:
                count += self.dp(i+1, next_tight)
        self.memo[i][tight] = count
        return count