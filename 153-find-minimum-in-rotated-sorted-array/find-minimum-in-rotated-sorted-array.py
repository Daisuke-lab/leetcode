class Solution:
    def findMin(self, nums: List[int]) -> int:
        queue = collections.deque()
        queue.append((0, len(nums) - 1))
        while queue:
            l, r = queue.popleft()
            m = (l + r) // 2
            #print(l, m, r)
            if m+1 < len(nums) and nums[m] > nums[m+1]:
                return nums[m+1]
            elif m > 0 and nums[m-1] > nums[m]:
                return nums[m]
            else:
                if l <= m - 1:
                    queue.append((l, m-1))
                if m + 1 <= r:
                    queue.append((m+1, r))
        return nums[0]
        