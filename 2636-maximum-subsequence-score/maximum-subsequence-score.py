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
        res, prefixSum, minHeap = 0, 0, []

        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(minHeap)                           
        return res
