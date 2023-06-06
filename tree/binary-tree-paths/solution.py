# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.outputs = set([])
        self.recursion(root, "")
        return self.outputs


    def recursion(self, root, output):
        if root is None:
            return 
        elif root.left is None and root.right is None:
            output = f"{output}->{root.val}"
            self.outputs.add(output[2:])

        else:
            self.recursion(root.right, f"{output}->{root.val}")
            self.recursion(root.left, f"{output}->{root.val}")