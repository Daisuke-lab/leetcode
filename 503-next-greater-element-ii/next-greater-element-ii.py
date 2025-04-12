class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1 for i in range(len(nums))]
        # monotonic decreasing stack
        stack = []
        for i in range(len(nums)*2):
            i = i % len(nums)
            # when you see bigger num
            while stack and nums[stack[-1]] < nums[i]:
                j = stack.pop()
                answer[j] = nums[i]
            stack.append(i)
        return answer
            
                
                
        