# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.prune(root)


    def prune(self, root):
        if root is None:
            return 
        else:
            root.left = self.prune(root.left)
            root.right = self.prune(root.right)
            if root.left is None and root.right is None and root.val == 0:
                return None
            else:
                return root
                