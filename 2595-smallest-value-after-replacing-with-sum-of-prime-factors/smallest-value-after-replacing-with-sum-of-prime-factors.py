class Solution:
    def smallestValue(self, n: int) -> int:
        prev = None
        curr = None
        nxt = n
        while prev != nxt:
            prev = nxt
            curr = nxt
            nxt = 0
            for i in range(2,prev+1):
                while curr % i == 0:
                    nxt += i
                    curr //= i
        return prev