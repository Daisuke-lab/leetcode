# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        count = 0
        while fast.next:
            count += 1
            fast = fast.next
            if count > n:
                slow = slow.next
        if count == 0:
            return None
        else:
            slow.next = slow.next.next
        return dummy.next