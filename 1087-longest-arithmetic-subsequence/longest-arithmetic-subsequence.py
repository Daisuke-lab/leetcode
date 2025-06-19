class Solution:
    # first two numbers are important
    # first, second, i => O(n^3) 
    
    # calculate the gaps (n^2) 
    # choose starting point n
    # check it exists n
    # O(n^4)

    # hash_map
    # {gap: count}
    # you can always create a new gap O(n) for each
    # if gap doesn't exist: create gap memo[gap][prev]
    # if gap exists, 
    # memo[gap][prev] if prev - gap == curr => increment the count and update prev
    # memo[gap][prev] if not                => you can set new prev using curr
    def longestArithSeqLength(self, nums: List[int]) -> int:
        memo = {}
        max_length = 2
        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                gap = nums[j] - nums[i]
                if (gap, j) in memo:
                    length = memo[(gap, j)] + 1
                    max_length = max(max_length, length)
                    if (gap, i) not in memo or memo[(gap, i)] < length:
                        memo[(gap, i)] = length
                else:
                    if (gap, i) not in memo:
                        memo[(gap, i)] = 2
        #rint(memo)
        return max_length
