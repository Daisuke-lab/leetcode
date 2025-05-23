class Solution:
    # 2 DP?
    
    # Replace a value
    # when min is the same: if nums[i] is bigger than the replacing value, it's good
    # when min becomes smaller: new_num > min_gap * sum
    # when min becomes bigger: 
    
    # How about reverse thinking
    # let's decide you want to add 100%
    # k can decrease
    # but you can not split list
    # What do you want to return => sum
    # but also want smallest num2 index
    # OK. return (max_sum, smallest_index)
    # compare smallest_index and finalize it
    # you also add current to max_sum
    # What do you want as args?
    # i, j and k
    # then it's O(K*n^2)


    # you fix num2 O(n)
    # make heap skipping the index O(2n)
    # collect sum from heap O(k)
    # O(k*n^2)

    # Why subsequence ??
    # your solution doesn't have to be subsequence
    # 
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_score = 0
        min_heap = []
        nums1_sum = 0
        reverse_sorted_nums = sorted(list(zip(nums1, nums2)), key=lambda nums: nums[1], reverse=True)
        for num1, num2 in reverse_sorted_nums:
            nums1_sum += num1
            heappush(min_heap, num1)
            if len(min_heap) == k:
                max_score = max(max_score, nums1_sum * num2)
                nums1_sum -= heappop(min_heap)                           
        return max_score
