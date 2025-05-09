# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you want to pass maxValue and minValue as args
    # when you go right, it updates minValue
    # when you go left, it updates maxValue
    # you want to create a new function
    # if both are
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursion(root, -float("inf"))[0]

    def recursion(self, root, curr):
        if root == None:
            return True, curr
        result, latest = self.recursion(root.left, curr)
        if result is True and latest < root.val:
            return self.recursion(root.right, root.val)
        else:
            return False, 0
            