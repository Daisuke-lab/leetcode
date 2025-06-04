# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you want to return string
    # if left is empty and right is empty, don't wrap it with ()
    # if right is empty, don't wrap it with ()
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        answer = f"{root.val}"
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left == "" and right == "":
            return answer
        elif left == "":
            answer += f"()({right})"
        elif right == "":
            answer += f"({left})"
        else:
            answer += f"({left})({right})"
        return answer
        