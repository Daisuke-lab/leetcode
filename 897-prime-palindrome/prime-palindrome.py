class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True

        # Generate palindrome candidates
        def generate_palindromes():
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

        # Iterate over palindromes and find the smallest prime palindrome >= n
        for palindrome in generate_palindromes():
            if palindrome >= n and is_prime(palindrome):
                return palindrome