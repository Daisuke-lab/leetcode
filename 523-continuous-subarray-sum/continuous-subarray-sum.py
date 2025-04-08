class Solution:
    # Brute Force => 2^n
    # DP => n^2
    # memo[(curr, i)] = true/false
    # because it's true or false, you can use set() instead
    # you can only carry around reminder
    # n*k

    # 2n
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0: -1}
        curr = 0

        for i, num in enumerate(nums):
            curr += num
            reminder = curr % k
            if reminder in rem_map and i- rem_map[reminder] > 1:
                return True
            if reminder not in rem_map:
                rem_map[reminder] = i
        return False
        
          