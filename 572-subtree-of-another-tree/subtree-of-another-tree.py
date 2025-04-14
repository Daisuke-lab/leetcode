# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root = self.serialize(root)
        subRoot = self.serialize(subRoot)
        return str(subRoot) in str(root)

    def serialize(self, root):
        if root is None:
            return {}
        else:
            return {"val": root.val, "left": self.serialize(root.left), "right": self.serialize(root.right)}