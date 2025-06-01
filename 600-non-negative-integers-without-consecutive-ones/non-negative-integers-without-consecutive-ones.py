class Solution:
    # Brute Force
    # n*logn

    # Digit DP 
    # 8 = 1000
    #  110 11 
    def findIntegers(self, n: int) -> int:
        self.memo = [[[
                -1 for k in range(3)]
                for j in range(2)]
                for i in range(32)]
        self.n = str(bin(n)[2:])
        #print(self.n)
        return self.dp(0, 1, 0)


    def dp(self, pos, tight, prev):
        if pos == len(self.n):
            return 1
        #print(pos, tight, prev)
        if self.memo[pos][tight][prev] != -1:
            return self.memo[pos][tight][prev]
        result = 0
        limit = int(self.n[pos]) if tight == 1 else 1
        for digit in range(limit + 1):
            if prev == 1 and digit == 1:
                continue
            
            next_tight = tight == 1 and limit == digit
            result += self.dp(pos + 1, next_tight, digit)
        self.memo[pos][tight][prev] = result
        return result

        