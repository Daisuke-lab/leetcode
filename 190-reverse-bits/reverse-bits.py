class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:]
        fills = 32 - len(bin_n)
        bin_n = "0"*fills + bin_n
        return int(bin_n[::-1], 2)
        