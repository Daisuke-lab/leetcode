class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * self.n)


    def update(self, index, value):
        # Set value at position index
        i = index + self.n
        self.tree[i] = value
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
            i //= 2

    def get_max(self, left, right):
        # Sum on interval [left, right]
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compress(arr):
            sortedArr = sorted(set(arr))
            order = []
            for num in arr:
                order.append(bisect_left(sortedArr, num))
            return order
        
        nums = compress(nums)
        n = len(nums)
        segTree = SegmentTree(n)

        LIS = 0
        for num in nums:
            curLIS = segTree.get_max(0, num - 1) + 1
            segTree.update(num, curLIS)
            LIS = max(LIS, curLIS)
        return LIS

        
        
            
        