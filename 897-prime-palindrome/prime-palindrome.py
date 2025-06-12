class Solution:
    def primePalindrome(self, n: int) -> int:
        palindromes = self.generate_palindrome()
        while True:
            palindrome = next(palindromes)
            print(palindrome)
            if self.is_prime(palindrome) and palindrome >= n:
                return palindrome

    def generate_palindrome(self):
        # 11, 22, 33
        # 101, 111, 121, 131, 141,...,202, 212
        # 1001, 1111, 1221, 1331, ..., 2002
        # 10001, 10101, 11011, 11111, 10201, 12021, 11211
        # 
        for i in range(10):
            yield i
        for i in range(1, 10):
            palindrome = str(i) + str(i)[::-1]
            yield int(palindrome)
        for i in range(1, 10):
            for j in range(10):
                palindrome = str(i) + str(j) + str(i)[::-1]
                yield int(palindrome)  

        for length in range(3, 10):
            if length % 2 == 0:
                half = length //2
                for i in range((half-1)**10 + 1, half**10):
                    palindrome = str(i) + str(i)[::-1]
                    yield int(palindrome)
            else:
                half = length //2
                for i in range((half-1)**10 + 1, half**10):
                    for j in range(1, 10):
                        palindrome = str(i) + str(j) + str(i)[::-1]
                        yield int(palindrome)

    def is_prime(self, n):
        if n in [0, 1]:
            return False
        if n in [2, 3]:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = ceil(math.sqrt(n)) + 2
        # limit 12 (11+1) (n=121)
        # 
        for i in range(6, limit, 6):
            if n % (i+1) == 0:
                return False
            if n % (i-1) == 0:
                return False
        return True
