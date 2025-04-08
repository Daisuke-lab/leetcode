class Solution:
    def primePalindrome(self, n: int) -> int:
        # Iterate over palindromes and find the smallest prime palindrome >= n
        for palindrome in self.generate_palindromes():
            if palindrome >= n and self.is_prime(palindrome):
                return palindrome

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        # Only check for divisors up to sqrt(n)
        # and use 6k ± 1 optimization
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    # Generate palindrome candidates
    def generate_palindromes(self):
        for i in range(1, 10):  # Single digit palindromes
            yield i
        for length in range(1, 6):  # Palindromes up to 10^8
            # Odd length palindromes
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                yield int(s + s[-2::-1])
            # Even length palindromes
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                yield int(s + s[::-1])

        