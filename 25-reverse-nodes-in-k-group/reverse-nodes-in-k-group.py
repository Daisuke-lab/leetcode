# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # two pointers are unrealistic because it's reverse
        # you can just reverse with O(n) using prev
        # you also want to maintain the next starting point
        #
        if k == 1:
            return head
        dummy = ListNode(0, 0)
        slow = dummy
        fast = ListNode(0, head)
        starting_point = head
        count = 0
        while fast:
            while count != k and fast:
                count += 1
                fast = fast.next
                if count == 1:
                    starting_point = fast
            if fast is None:
                slow.next = starting_point
                fast = None
            else:
                _next = fast.next
                fast.next = None
                reversed_node = self.reverse_list(starting_point)
                slow.next = reversed_node
                slow = starting_point
                starting_point.next = _next
                fast = starting_point
            count = 0
            starting_point = None

        return dummy.next
    def reverse_list(self, node):
        prev = None
        while node:
            _next = node.next
            node.next = None
            if prev is None:
                prev = node
            else:
                node.next = prev
                prev = node
            node = _next
        return prev
                
            
        
        