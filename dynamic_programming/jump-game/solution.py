class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #とにかくlast indexを超えればいい。ピタッと着地する必要なない。
        current = 0
        for  i in range(len(nums)):
            if i > current: return False
            #currentに今最大で届くindexを残しておく。
            current = max(current, i + nums[i])

        return True
        