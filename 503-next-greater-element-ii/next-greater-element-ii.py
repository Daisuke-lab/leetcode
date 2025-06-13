class Solution:
    # find max
    # not-increasing stack
    # (i, num)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        answer = [-1 for i in range(length)]
        nums = nums + nums
        max_num = max(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                j, prev_num = stack.pop()
                answer[j] = num
            if num != max_num:
                i %= length
                stack.append((i, num))
        return answer
                
                
        