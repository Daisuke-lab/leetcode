class Solution:
    # Brute Force solution
    # try every partition 
    # O(2^n)

    # DP
    # i and j
    # you want to return count
    # you also want to return min number and max number
    # O(n^2)

    # args: i, j
    # output: count, min_num, max_num

    # base case: i = j => return 1, nums[i], nums[j]
    # merge: find curr max and min and if it works, + 1
    
    # can you do bottom up
    def countPartitions(self, A: List[int], k: int) -> int:
        n = len(A)
        mod = 10**9 + 7
        dp = [1] + [0] * n
        acc = 1
        minq = deque()
        maxq = deque()
        i = 0
        for j in range(n):
            while maxq and A[j] > A[maxq[-1]]:
                maxq.pop()
            maxq.append(j)
            while minq and A[j] < A[minq[-1]]:
                minq.pop()
            minq.append(j)

            while A[maxq[0]] - A[minq[0]] > k:
                acc = (acc - dp[i]) % mod
                i += 1
                if minq[0] < i:
                    minq.popleft()
                if maxq[0] < i:
                    maxq.popleft()
            dp[j + 1] = acc
            acc = (acc*2) % mod
        return dp[n]        