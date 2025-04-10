class Solution:
    # you can not choose too far numbers
    # tab = i[] i: max sum
    # iterate i and check max (i-k ~ i) and find the max and plus current
    # 
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        max_sum = nums[0]
        # decreasing queue
        queue = collections.deque()
        for i in range(len(nums)):
            #print(queue)
            if queue and i - queue[0][0] > k:
                queue.popleft()

            curr_sum = nums[i]
            if queue and queue[0][1] > 0:
                curr_sum += queue[0][1]
            while queue and queue[-1][1] < curr_sum:
                queue.pop()
            queue.append((i, curr_sum))
            max_sum = max(max_sum, curr_sum)
        return max_sum

        