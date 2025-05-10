# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                left_most_child = self.get_most_left_node(root.right)
                #print(left_most_child)
                if root.right == left_most_child:
                    left_most_child.right = None
                else:
                    left_most_child.right = root.right
                return left_most_child
            else:
                right_most_node = self.get_most_right_node(root.left)
                if right_most_node != root.left:
                    right_most_node.left = root.left 
                right_most_node.right = root.right
                return right_most_node
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def get_most_left_node(self, root):
        if root.left is None:
            return root
        left_most_node = self.get_most_left_node(root.left)
        if root.left == left_most_node:
            root.left = left_most_node.right
            left_most_node.right = None
        return left_most_node

    
    def get_most_right_node(self, root):
        if root.right is None:
            return root
        right_most_node = self.get_most_right_node(root.right)
        if root.right == right_most_node:
            root.right = right_most_node.left
            right_most_node.left = None
        return right_most_node
    
