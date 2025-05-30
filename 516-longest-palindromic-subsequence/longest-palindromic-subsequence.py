class Solution:
    # Subsequence pattern => O(2^n)
    # Palindrome check => O(n)
    # Time complexity is O(2^n) * n

    # check from the middle, if not palindrome, you can drop either left or right
    # so it's recursive 
    # you want to pass left, right as args
    # if left = right, shift it
    # if left != right, you can shift left or right
    # if left or right index is out of the bound, collect the length
    # you want to cache by left and right
    
    # out of bound => 0
    # left != right => return child
    # left == right = return child + 2
    # O(n^3)
    def longestPalindromeSubseq(self, s: str) -> int:
        self.grid = [[-1 for j in range(len(s))] for i in range(len(s))]
        self.s = s
        return self.dp(0, len(s) -1)

    def dp(self, l, r):
        if r < l:
            return 0
        if l == r:
            return 1
        elif self.grid[l][r] != -1:
            return self.grid[l][r]
        length = 0
        if self.s[l] == self.s[r]:
            length += 2
            length += self.dp(l+1, r-1)
        else:
            length = max(self.dp(l+1, r), self.dp(l, r-1))
        self.grid[l][r] = length
        return length       