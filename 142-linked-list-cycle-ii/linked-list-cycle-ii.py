# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = self.find_cycle(head)
        if node is None:
            return None
        while node != head:
            head = head.next
            node = node.next
        #print(head.val)
        return head

    def find_cycle(self, head):
        slow = head.next
        fast = head.next.next if head.next else None
        while fast is not None and slow != fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
        return fast
        