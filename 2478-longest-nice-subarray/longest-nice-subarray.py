class Solution:
    # you need to keep OR num
    # you need queue and then XOR to deliminate 
    def longestNiceSubarray(self, nums: List[int]) -> int:
        stack_queue = []
        max_length = 0
        or_num = 0
        for i in range(len(nums)):
            # no overlap for 1 position
            if or_num & nums[i] == 0:
                # keep all one position with OR
                or_num = or_num | nums[i]
                stack_queue.append(nums[i])
            else:
                max_length = max(max_length, len(stack_queue))
                while or_num & nums[i] != 0:
                    removing_num = stack_queue.pop(0)
                    or_num = or_num ^ removing_num
                or_num = or_num | nums[i]
                stack_queue.append(nums[i])
        max_length = max(max_length, len(stack_queue))
        return max_length
                
            