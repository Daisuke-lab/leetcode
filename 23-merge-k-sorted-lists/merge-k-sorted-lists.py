# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n*m) n: the length of list, m: the length of node
    # O(n) + O(logn*m), O(n): heapify, O(logm*n): m*n=total nodes => you add value to heap by log
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_lists = lists
        if len(lists) == 0 or lists is None:
            return None
        while len(merged_lists) != 1:
            new_merged_lists = []
            for i in range(0, len(merged_lists), 2):
                node1 = merged_lists[i]
                node2 = merged_lists[i+1] if i+1 < len(merged_lists) else None
                merged_node = self.mergeTwo(node1, node2)
                new_merged_lists.append(merged_node)
            merged_lists = new_merged_lists
        return merged_lists[0]
    
    def mergeTwo(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            head = dummy = ListNode()
            while list1 or list2:
                if list1 is None:
                    head.next = list2
                    list2 = None
                    continue
                if list2 is None:
                    head.next = list1
                    list1 = None
                    continue
                if list1.val < list2.val:
                    _next = list1.next
                    list1.next = None
                    head.next = list1
                    list1 = _next
                else:
                    _next = list2.next
                    list2.next = None
                    head.next = list2
                    list2 = _next
                head = head.next
        return dummy.next
