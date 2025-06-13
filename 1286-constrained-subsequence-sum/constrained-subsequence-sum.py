class Solution:
    # Brute Force
    # get max sum til i - k
    # if it is negative, you don't include it 
    # if it is positive, you include it
    # but you can include i -1, i -2, i-3, ..i-k
    # so this will be the deque

    # non-increasing queue
    # (i, num)
    # you have choice 
    # case1: want to include prefix to maintian neighborhood
    # case2: remove the prefix 
    # what do you want?? => I want the max sum of prefix
    # To do that, you need deque
    # get the max sum from previous block
    # but index matters
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = collections.deque()
        sums = [0 for i in range(len(nums))]
        for i, num in enumerate(nums):
            while queue and queue[0][0] < i - k:
                queue.popleft()
            if queue and queue[0][1] > 0:
                sums[i] = queue[0][1] + num
            else:
                sums[i] = num
            while queue and queue[-1][1] < sums[i]:
                queue.pop()
            queue.append((i, sums[i]))
        return max(sums)