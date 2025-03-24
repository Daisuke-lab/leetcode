# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n*m) n: the length of list, m: the length of node
    # O(n) + O(logn*m), O(n): heapify, O(logm*n): m*n=total nodes => you add value to heap by log
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()
        heap = []
        for i, node in enumerate(lists):
            if node:
                # If node.val is exactly same, i is used for sorting, which doesn't matter
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, _, node = heapq.heappop(heap)
            head.next = node
            head = node

            node = node.next
            if node:
                heapq.heappush(heap, (node.val, _, node))
        return dummy.next
