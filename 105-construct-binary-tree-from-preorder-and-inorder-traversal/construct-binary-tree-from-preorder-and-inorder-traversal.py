# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode()
        queue = collections.deque()
        queue.append((dummy, "left"))
        node_map = {}
        while preorder:
            root, direction = queue.pop()
            val = preorder.pop(0)
            node = TreeNode(val)
            node_map[val] = node
            if direction == "left":
                root.left = node
            else:
                root.right = node
            if val != inorder[0]:
                queue.append((node, "left"))
            else:
                next_node = node
                while inorder and inorder[0] in node_map:
                    next_node = node_map[inorder.pop(0)]
                queue.append((next_node, "right"))
        
        return dummy.left

    
        