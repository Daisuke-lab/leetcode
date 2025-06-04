# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you want to pass curr height
    # you want to make this traversal consistent throughout the recursion => return this with node
    # check height * "-" and then you see the number. If you see anycharacter between them, return null
    
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.recover(traversal)[0]

    def recover(self, traversal, height=0):
        for i in range(height):
            if i >= len(traversal) or traversal[i] != "-":
                return None, traversal
        if traversal[height] == "-":
            return None, traversal
        num, traversal = self.extract_number(traversal, height)
        node = TreeNode(num)
        node.left, traversal = self.recover(traversal, height + 1)
        node.right, traversal = self.recover(traversal, height + 1)
        return node, traversal

    def extract_number(self, traversal, height):
        num = ""
        for i in range(height, len(traversal)):
            if traversal[i] != "-":
                num += traversal[i]
            else:
                break
        return int(num), traversal[i:]