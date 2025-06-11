class Solution:
    # how to get divisors quickly
    # how to check if it's prime number or not
    def smallestValue(self, n: int) -> int:
        prev = None
        curr = None
        _next = n
        while prev != _next:
            prev = _next
            curr = _next
            _next = 0
            for i in range(2, prev+1):
                while curr % i == 0:
                    _next += i
                    curr //= i
        return prev