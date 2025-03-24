# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you also want to pass max value besides root as args
    # create a new function for that
    # you also want to maintain global count variable
    # the initial value for max is -float("inf") since the n range starts from 1
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, -float("inf"))
        return self.count


    def dfs(self, root, max_value):
        if root is None:
            return 
        elif root.val >= max_value:
            self.count += 1
            max_value = root.val
        self.dfs(root.left, max_value)
        self.dfs(root.right, max_value)