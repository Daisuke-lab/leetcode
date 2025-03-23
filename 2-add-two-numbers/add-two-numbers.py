# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        factor = 1
        l1_num = 0
        l2_num = 0
        while l1 or l2:
            if l1:
                l1_num += l1.val * factor
                l1 = l1.next
            if l2:
                l2_num += l2.val * factor
                l2 = l2.next
            factor *= 10
        total = l1_num + l2_num
        head = dummy = ListNode()
        if total == 0:
            return ListNode(0) 
        while total:
            num = total % 10
            node = ListNode(num)
            head.next = node
            head = node
            total -= num
            total //= 10
        return dummy.next
        