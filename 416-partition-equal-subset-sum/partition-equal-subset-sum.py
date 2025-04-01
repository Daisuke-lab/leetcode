class Solution:
    # get sum first.
    # if it's odd return false
    
    # Brute Force
    # you have two choices at every element. You choose the element or not
    # Time complexity is O(2^n)
    
    # Is sort helpful ??
    # this is actually combination sum question
    # reduce target by selecting num, and also remove selected num 
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2:
            return False
        target = num_sum // 2
        sum_set = set([0])
        for num in nums:
            temp = set(sum_set)
            for _sum in temp:
                sum_set.add(_sum + num)
                if target in sum_set:
                    return True
        return False
        

        