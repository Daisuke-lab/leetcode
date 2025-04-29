class Solution:
    def test(self, m):
            l = max(m - self.index, 0)
            length = m - l + 1
            res = length * (l + m) / 2
            r = max(m - ((self.n - 1) - self.index), 0)
            length = m - r + 1
            res += length * (m + r) / 2
            return res - m

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.n = n
        self.index = index

        # Because you don't want to calculate flattened area [2,1,1,1]
        #                                                      ------
        # you assume it has all one at foundation (maxSum -=n)
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        result = left + 1
        return result