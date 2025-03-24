# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # If root.val == subRoot.val => you want to continue to check if it's the same tree (isSameTree)
    # If root.val != subRoot.val => you want to check with left and right
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_sub_root = self.serialize(subRoot)
        return serialized_sub_root in serialized_root