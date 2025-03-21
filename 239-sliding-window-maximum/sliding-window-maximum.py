class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # calculate max value every time 
        # Time Complexity is O((n-k)*k) => n^2/4

        # Want to do by linear O(n)
        # you want to know max size but the list is changing => Max Heap?
        # but you want to remove num even if it's not max value.
        # Eg. if you don't remove second biggest num when shifting, when the biggest num is removed
        # the actual max value is different (second biggest can be treated as a new biggest num)
        # Heap might not be effective as it looks
        # Time complexity O(2nlogn) logn: insert new num, logn: delete fallen num
        
        # 1. keep track of max num, and i regardless of window size
        # 2. calculate new max num
        # in worst case, you have to calculate new max (n^2/4)

        answer = []
        queue = collections.deque()
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i >= k:
                removing_num = nums[i-k]
                if queue[0] == removing_num:
                    queue.popleft()
            if i >= k - 1:
                answer.append(queue[0])
        return answer
                