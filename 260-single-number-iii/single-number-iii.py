class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total_xor = self.get_total_xor(nums)
        i = self.get_first_bit_location(total_xor)
        zero_xor = 0
        one_xor = 0
        for num in nums:
            have_bit = (num & (1 << i)) != 0
            if have_bit:
                one_xor ^= num
            else:
                zero_xor ^= num
        return [zero_xor, one_xor]


    def get_total_xor(self, nums):
        total_xor = 0
        for num in nums:
            total_xor ^= num
        return total_xor

    def get_first_bit_location(self, num):
        i = 0
        while True:
            have_bit = (num & (1 << i)) != 0
            if have_bit:
                return i
            else:
                i += 1