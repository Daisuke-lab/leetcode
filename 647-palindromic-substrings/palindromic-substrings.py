class Solution:
    # You can expand the palindrome size from 1 to n
    # You can return the size accordingly
    # you keep adding the child size to your current size
    # how can you avoid double count ?? => hashset
    # you can speed up is_palindrome by cache
    def countSubstrings(self, s: str) -> int:
        self.memo = {}
        self.counted = set()
        self.s = s
        return self.dp(0)

    def dp(self, i):
        if i in self.counted:
            return 0
        self.counted.add(i)
        count = 0
        for k in range(i, len(self.s)+1):
            substring = self.s[i:k]
            if self.is_palindrome(substring):
                #print(substring)
                count += 1
            count += self.dp(k)
        return count

    def is_palindrome(self, s):
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True
        if len(s) == 2 and s[0] == s[-1]:
            return True
        if s in self.memo:
            return self.memo[s]
        result = False
        if s[0] == s[-1]:
            result = self.is_palindrome(s[1:-1])
        self.memo[s] = result
        return result
        