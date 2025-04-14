# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.recursion(root, subRoot, False)

    def recursion(self, root, subRoot, started):
        if root is None and subRoot is None:
            return True
        elif root is None:
            return False
        elif subRoot is None:
            return False
        elif root.val != subRoot.val and started is False:
            return self.recursion(root.left, subRoot, False) or self.recursion(root.right, subRoot, False)
        elif root.val != subRoot.val and started:
            return False
        elif root.val == subRoot.val and started is False:
            result = self.recursion(root.left, subRoot.left, True) and self.recursion(root.right, subRoot.right, True)
            if result:
                return True
            else:
                return self.recursion(root.left, subRoot, False) or self.recursion(root.right, subRoot, False)
        else:
            return self.recursion(root.left, subRoot.left, True) and self.recursion(root.right, subRoot.right, True)