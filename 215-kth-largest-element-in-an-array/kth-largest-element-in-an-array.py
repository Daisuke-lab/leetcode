class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # you want to create min heap that has k nodes
        # If new value is smaller than min size and heap is complete, you don't need the insertion
        return heapq.nlargest(k, nums)[-1]