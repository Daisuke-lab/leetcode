# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        current = head
        self.count = 0
        self.recursion(current, nums)
        return self.count
        

    def recursion(self, head, nums, consecutive=False):
        if head is None:
            return
        elif head.val in nums:
            nums.remove(head.val)
            if consecutive is False:
                self.count += 1
                consecutive = True
        else:
            consecutive = False

            
        self.recursion(head.next, nums, consecutive)