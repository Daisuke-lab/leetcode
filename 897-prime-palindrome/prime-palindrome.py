class Solution:
    def primePalindrome(self, n: int) -> int:
        if 8 <= n <= 11:
            return 11

        half_size = len(str(n)) // 2
        for i in range(10**half_size, 10**5):
            palindrome = int(str(i) + str(i)[-2::-1])
            if self.is_prime(palindrome) and palindrome >= n:
                return palindrome


    def is_prime(self, n):
        if n < 2:
            return False
        elif n < 4:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        max_divisor = int(math.sqrt(n)) + 1
        for i in range(5, max_divisor, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True