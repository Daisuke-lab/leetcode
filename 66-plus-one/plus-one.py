class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i]
            if i == len(digits) -1:
                digit += 1
            else:
                digit += carry
            carry = digit // 10
            digit = digit % 10
            digits[i] = digit
        if carry != 0:
            digits.insert(0, carry)
        return digits
            
                            
        