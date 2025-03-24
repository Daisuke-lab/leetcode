# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # If root.val == subRoot.val => you want to continue to check if it's the same tree (isSameTree)
    # If root.val != subRoot.val => you want to check with left and right
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None:
            return False
        elif subRoot is None:
            return False
        
        if root.val == subRoot.val:
            result = self.isSameTree(root, subRoot)
            if result:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        else:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)