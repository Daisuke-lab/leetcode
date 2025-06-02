class Solution:
    # By reverse seorting by num2, you fix the min number in nums2 (reduicing variables in formula)
    # By maintaining heap, and always pushing to the heap in each index, it makes sure curr num2 can be chosen
    # BY using min-heap, you are making sure you always remove the smallest number
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key= lambda num: num[1], reverse=True)
        curr_sum = 0
        max_value = 0
        min_heap = []
        for num1, num2 in nums:
            curr_sum += num1
            heapq.heappush(min_heap, num1)
            if len(min_heap) == k:
                max_value = max(max_value, curr_sum*num2)
                curr_sum -= heapq.heappop(min_heap)
        return max_value          

