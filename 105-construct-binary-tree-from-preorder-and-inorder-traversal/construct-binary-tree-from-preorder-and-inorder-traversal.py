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

        # you can not add simply to left in the first place
        # if preorder[0] and inorder[0] are the same, please go right.
        tree = dummy = TreeNode(float("inf"))
        node_map = {}
        queue = collections.deque()
        queue.append((0, "left"))
        while queue:
            i, direction = queue.popleft()
            if i >= len(preorder):
                continue
            node = TreeNode(preorder[i])
            node_map[node.val] = node
            if direction == "left":
                tree.left = node
                tree = node
            else:
                tree.right = node
                tree = node
            go_right = False
            while inorder and inorder[0] in node_map:
                go_right = True
                tree = node_map[inorder.pop(0)]
            if go_right:
                queue.append((i+1, "right"))
            else:
                queue.append((i+1, "left"))
        
        return dummy.left
            
            
        
                

    
        