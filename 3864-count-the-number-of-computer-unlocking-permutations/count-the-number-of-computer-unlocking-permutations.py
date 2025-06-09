class Solution:
    def countPermutations(self, A: List[int]) -> int:
        if A[0] > min(A) or A.count(A[0]) > 1:
            return 0
        return factorial(len(A) - 1) % (10 ** 9 + 7)