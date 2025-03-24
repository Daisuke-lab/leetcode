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
        return self.dfs(root, -float("inf"), float("inf"))

    def dfs(self, root, min_value, max_value):
        if root is None:
            return True
        if root.val <= min_value:
            return False
        elif root.val >= max_value:
            return False
        return self.dfs(root.left, min_value, root.val) and self.dfs(root.right, root.val, max_value)