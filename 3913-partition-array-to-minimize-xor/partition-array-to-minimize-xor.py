class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        @cache
        def dp(index, parts):
            if parts == 0 and index == n:
                return 0
            if parts == 0 or index == n:
                return float('inf')

            current = 0
            answer = float('inf')

            for i in range(index, n - (parts-1)):
                current ^= nums[i]
                next = dp(i + 1, parts - 1)
                maximum = max(current,next)
                answer = min(answer, maximum)
            return answer
        return dp(0,k)