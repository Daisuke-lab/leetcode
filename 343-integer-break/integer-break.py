class Solution:
    # it is like partition
    #  1 to n would be the input
    # what is the base case?
    # n = 2 is  
    # if n < 2, it is going to be 0
    # you can not produce current result from child

    # Brute Force
    # generate all the ways to split
    # calculate product

    # you want to save the max proeuct still
    # if it is equal to original n you can say no
    
    def integerBreak(self, n: int) -> int:
        self.memo = {}
        self.max_product = 0
        self.n = n
        #self.dp(n)
        return self.dp(n, True)
        


    def dp(self, n, flag=False):
        
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        max_product = 0
        start = 1 if flag else 0
        for i in range(start, n):
            product = self.dp(i) * (n - i)
            max_product = max(max_product, product)
        self.memo[n] = max_product
        return max_product