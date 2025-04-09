class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11

        half_size = len(str(n)) // 2
        for x in range(10 ** half_size, 10**5):
            #print(x)
            palindrome = int(str(x) + str(x)[-2::-1])
            #print(palindrome)
            if palindrome >= n and self.isPrime(palindrome):
                return palindrome

                
    def isPrime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

        