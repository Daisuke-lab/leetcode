# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # you might need dummy node
    # you need to maintian the node just before reversing
    
    # 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode()
        dummy.next = head
        root = dummy
        while head:
            count += 1
            if count == k and head:
                _next = head.next
                new_head, new_tail = self.reverse(root.next, head)
                root.next = new_head
                new_tail.next = _next
                root = new_tail
                head = new_tail
                count = 0
            head = head.next
        return dummy.next

    def reverse(self, head, tail):
        new_tail = head
        new_head = None
        while head != tail:
            _next = head.next
            head.next = None
            if new_head == None:
                new_head = head
            else:
                head.next = new_head
                new_head = head
            head = _next
        tail.next = new_head
        new_head = tail
        return new_head, new_tail
        
