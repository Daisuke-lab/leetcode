class Solution:
    def search(self, nums: List[int], target: int) -> int:
        queue = collections.deque()
        i = 0
        j = len(nums) -1 
        queue.append((i, j, False))
        while queue:
            l, r, pivot_found = queue.popleft()
            next_pivot_found = pivot_found
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # pivot found
            if m < len(nums) - 1 and nums[m] > nums[m+1]:
                next_pivot_found = True
            elif m > 0 and nums[m-1] > nums[m]:
                next_pivot_found = True
            if (l <= m - 1) and (pivot_found is False or target < nums[m]):
                queue.append((l, m-1, next_pivot_found))
            if r >= m + 1 and (pivot_found is False or target > nums[m]):
                queue.append((m+1, r, next_pivot_found))

        return -1