class Solution:
    # you have 2 patterns. Do you include current character or not?
    # it's O(2^n)
    
    # you can decrese this O(m*n)
    # you can create memo[i][j] *i=s's index, j=t's index
    # you want to memoize the "count"
    # the base case could be s="", t="", it is 1
    # 
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        self.ROW = len(s)
        self.COL = len(t)
        memo = [[0 for j in range(self.COL)] for i in range(self.ROW)]

        for j in range(self.COL -1, -1, -1):
            for i in range(self.ROW -1, -1, -1):
                if i != self.ROW -1:
                    memo[i][j] = memo[i+1][j]        
                if j == self.COL - 1 and s[i] == t[j]:
                    memo[i][j] += 1
                if i != self.ROW - 1 and j != self.COL - 1 and memo[i+1][j+1] != 0 and s[i] == t[j]:
                    memo[i][j] += memo[i+1][j+1]
        #print(memo)
        return memo[0][0]    