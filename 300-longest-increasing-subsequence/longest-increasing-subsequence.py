class Solution:
    # you want to start faster to elongate length
    # you want to minimize start to collect elements as many as possible
    # O(N) is the goal
    # Brute force is O(N)
    
    # You want to start from left is bigger than you
    # You want to start from right is bigger than you or equal
    # => equal => whereever you want to start
    # you can skip number if you go through with smaller number already
    # the worst case is O(N^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        answer = [1 for i in range(len(nums))]
        for i in range(len(nums) -2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    answer[i] = max(answer[i], answer[j] + 1)
        return max(answer)

        