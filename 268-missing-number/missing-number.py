class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        max_num = -1
        for num in nums:
            unique = 1 << num
            res |= unique
            max_num = max(max_num, num)
        bin_res = bin(res)[2:]
        #print(bin_res)
        mask = "1" * len(bin_res)
        mask = int(mask, 2)
        if res ^ mask == 0:
            return max_num+1
        return int(log2(res ^ mask))
        