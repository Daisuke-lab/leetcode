class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1

        curr = 1
        while n > 0:
            if n % 2 == 0:
                x = x*x
                n /= 2
            curr *= x
            n -= 1
        return curr
        