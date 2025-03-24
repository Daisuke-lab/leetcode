# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Can you tell which way you should go (left or right) ?? => NO
        # if you look for number, you can do it but not for Kth number
        
        # you can keep going to left, if there is no way to go left, you can go right
        # If there is no child, you keep the node to list
        # if the number of list is the same as k, return the last one
        # create a new function to separate global variable (visited)
        self.visited = []
        self.answer = None
        self.k = k
        self.dfs(root)
        print(self.visited)
        return self.answer

    def dfs(self, root):
        if self.answer is not None:
            return 
        if root is None:
            return
        self.dfs(root.left)
        self.visited.append(root)
        if len(self.visited) == self.k:
            self.answer = root.val
        self.dfs(root.right)
            


                