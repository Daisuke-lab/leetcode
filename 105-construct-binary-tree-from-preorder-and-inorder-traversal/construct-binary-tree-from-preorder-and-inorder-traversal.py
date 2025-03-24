# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # you keep left making i in preorder as root
        # if you find the same number in inorder, it means left is None.
        # you go back to the parent until you see the same number in inorder (hashmap)
        # and then go right once and keep going left again.

        # 1. pop from preorder
        # 2. add to the tree, and hashmap
        # 3. check if it's the same as inorder
        # 3.1 keep poping (root) until you find the num in hashmap
        # 4. set root.right = next preorder num 
        # 5. go right
        # 6. go back to 1

        # TAKE AWAY
        # simpel while loop doesn't tell you which direction you should add,
        # The only way to know is set some flag (direction)

        tree = dummy = TreeNode(float("inf"))
        node_map = {}
        direction = "left"
        while preorder:
            val = preorder.pop(0)
            node = TreeNode(val)
            node_map[node.val] = node
            if direction == "left":
                tree.left = node
                tree = node
            else:
                tree.right = node
                tree = node
            direction = "left"
            while inorder and inorder[0] in node_map:
                direction = "right"
                tree = node_map[inorder.pop(0)]
        
        return dummy.left
            
            
        
                

    
        