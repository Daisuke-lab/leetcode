"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.node_map = {}
        return self.dfs(head)
        
        
    def dfs(self, head):
        key = hash(head)
        if head is None:
            return None
        elif key in self.node_map:
            return self.node_map[key]
        else:
            copy = ListNode(head.val)
            self.node_map[key] = copy
            random_copy = self.dfs(head.random)
            next_copy = self.dfs(head.next)
            copy.random = random_copy
            copy.next = next_copy
            return copy
            