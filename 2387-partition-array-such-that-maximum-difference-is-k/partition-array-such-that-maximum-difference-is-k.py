class Solution:
    # Brute Force
    # 2^n to create one subsequence
    # O(n) to keep doing the above until array is empty

    # Greedy
    # can be sorted
    # 

    # you want to keep track of the number of partitions so far
    # you also want to compare
    # what if curr can be assigned to multiple partition
    
    def partitionArray(self, nums: List[int], k: int) -> int:
        partitions = 1
        nums.sort()
        min_num = None
        for num in nums:
            if min_num is None:
                min_num = num
            elif num - min_num > k:
                min_num = num
                partitions += 1
        return partitions