class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [ True for _ in range(right + 1) ]
        # Base case initialization
        is_prime[0] = False
        is_prime[1] = False
        
        upper_bound = (right // 2) + 1
        # if it's 10, range(2, 6)
        for i in range(2, upper_bound):
            # 1. range(4, 10, 2), 2. range(9, 10, 3)
            for j in range(i*i, right+1, i):
                is_prime[j] = False
        primes = [i for i in range(left, right+1) if is_prime[i]]

        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]
        
        return result