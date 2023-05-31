# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """       

        self.startnode = None
        self.prev = None
        self.lastnode = None
        self.dfs(root)
        # swap the nodes that are not in place
        if self.startnode and self.lastnode:
            self.startnode.val, self.lastnode.val = self.lastnode.val, self.startnode.val
        
    def dfs(self, root):
        if not root:
            return 
        # go to left  (inorder step 1)  
        self.dfs(root.left)
        
        # do processing....(inorder step 2)
        # get the first node where the sorted order is broken the first time and the last time
        if self.prev and self.prev.val > root.val:
            if not self.startnode:
                self.startnode = self.prev
            self.lastnode = root
            
        self.prev = root
        
        # go to right (inorder step 3)    
        self.dfs(root.right)