class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # you can nost sort due to the follow-up constraint
        next_value_map = self.build_map_with_descending_monotonic_stack(nums2)
        answer = []
        for i in range(len(nums1)):
            answer.append(next_value_map.get(nums1[i], -1))
        return answer

    def build_map_with_descending_monotonic_stack(self, nums):
        stack = []
        next_value_map = {}
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                # what if [4,5,6] and 9 came and after that 7 is in. 7 is the next big value for 6
                # The question says "the first greater element that is to the right of x in the same array."
                smallest = stack.pop()
                next_value_map[smallest] = nums[i]
            stack.append(nums[i])
        return next_value_map