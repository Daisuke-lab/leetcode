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
        return self.recursion(root, -float("inf")) != float("inf")

    def recursion(self, root, curr):
        if root == None:
            return curr
        latest = self.recursion(root.left, curr)
        if latest != float("inf") and latest < root.val:
            return self.recursion(root.right, root.val)
        else:
            return float("inf")
            