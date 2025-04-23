# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dp 
    # what do you want to return, max that I can not include myself and max that I can include my self
    # what do you want as args, root should be fine
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dp(root))

    def dp(self, root):
        if root is None:
            return 0, 0
        unsafe_left_result, safe_left_result = self.dp(root.left)
        unsafe_right_result, safe_right_result = self.dp(root.right)
        
        unsafe_result = root.val + safe_left_result + safe_right_result
        safe_result = max(unsafe_left_result, safe_left_result) + max(unsafe_right_result, safe_right_result)
        return unsafe_result, safe_result
        
        