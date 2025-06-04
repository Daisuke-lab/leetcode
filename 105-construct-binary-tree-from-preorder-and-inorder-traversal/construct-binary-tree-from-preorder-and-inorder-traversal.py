# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # case1: keep going to the left
    # case2: keep popping from inorder until you get unvisited node
    # case3: go right once and continue the process

    # variables
    # i: keep tracking of preorder 
    # j: keep tracking of inorder
    # queue: (direction, parent)
    # visited: set()
    
    # base case
    # queue is not empty (or i and j is inbound)
    # 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        j = 0
        queue = collections.deque()
        dummy = TreeNode()
        node_map = {}
        queue.append((dummy, "left"))
        visited = set()
        while queue:
            parent, direction = queue.popleft()
            node = TreeNode(preorder[i])
            if direction == "left":
                parent.left = node
            elif direction == "right":
                parent.right = node
            i += 1
            visited.add(node.val)
            node_map[node.val] = node
            #queue.append((node, "left"))

            direction = "left"
            next_parent = node
            while j < len(inorder) and inorder[j] in visited:
                next_parent = node_map[inorder[j]]
                j += 1
                direction = "right"
            if i < len(preorder) and j < len(inorder):
                queue.append((next_parent, direction))

        return dummy.left
                    

    
        