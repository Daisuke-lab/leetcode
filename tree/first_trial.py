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
        init_left, init_right = TreeNode(-float('inf')), TreeNode(float("inf"))
        wrongs = self.find_wrongs(root, init_left, init_right, [])
        #rootとleft, rightどちらをswapするべきか
        print(len(wrongs))
        if len(wrongs) == 1:
            wrongs[0][0].val, wrongs[0][1].val = wrongs[0][1].val, wrongs[0][0].val
        else:
            wrongs[0][0].val, wrongs[1][0].val = wrongs[1][0].val, wrongs[0][0].val


    def find_wrongs(self, root, left, right, wrongs):
        if root and left and right:
            if root.val <= left.val:
                wrongs.append((root, left))
                return wrongs
            elif root.val >= right.val:
                wrongs.append((root, right))
                return wrongs
            else:
                wrongs = self.find_wrongs(root.left, left, root, wrongs)
                wrongs = self.find_wrongs(root.right, root, right, wrongs)
                return wrongs
        return wrongs