class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {}
        rem = 0
        for i, num in enumerate(nums):
            rem = (rem + num) % k
            if rem == 0 and i + 1 >= 2:
                return True
            if rem in rem_map and i - rem_map[rem] >= 2:
                return True
            elif rem not in rem_map:
                rem_map[rem] = i
        return False
        
          