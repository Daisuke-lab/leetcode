class Solution:
    # how to get divisors quickly
    # how to check if it's prime number or not
    def smallestValue(self, n: int) -> int:
        primes = self.collect_primes(n)
        primes_set = set(primes)
        visited = set()
        while n not in primes_set and n not in visited:
            visited.add(n)
            factors = self.split_to_factors(n, primes)
            n = sum(factors)
        return n

    def split_to_factors(self, n, primes):
        factors = []
        for prime in primes:
            while n % prime == 0:
                n //= prime
                factors.append(prime)
            if n == 1:
                break
        return factors
        


    def collect_primes(self, n):
        primes = []
        memo = [1 for i in range(n + 1)]
        memo[0] = 0
        memo[1] = 0
        limit = ceil(math.sqrt(n)) + 1
        for i in range(2, limit):
            for j in range(i*2, n+1, i):
                memo[j] = 0
        for i, _ in enumerate(memo):
            if memo[i] == 1:
                primes.append(i)
        return primes