# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # you want to return q_found, p_found, node
    # if you are not neither p nor q, you search left and right, do left_q_found | right_q_found
    # and both are true and node is still -1, you set current node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a,b, result = self.dfs(root, p, q)
        return result

    def dfs(self, root, p, q):
        node = None
        if root is None:
            return False, False, None
        if root == p and root == q:
            return True, True, root
        elif root == p:
            p_left_found, q_left_found, left_node = self.dfs(root.left, p, q) 
            p_right_found, q_right_found, right_node = self.dfs(root.right, p, q)
            p_found = True
            q_found = q_left_found or q_right_found
            if p_found and q_found:
                if left_node is not None:
                    node = left_node
                elif right_node is not None:
                    node = right_node
                else:
                    node = root
        elif root == q:
            p_left_found, q_left_found, left_node = self.dfs(root.left, p, q) 
            p_right_found, q_right_found, right_node = self.dfs(root.right, p, q)
            p_found = p_left_found or p_right_found
            q_found = True
            if p_found and q_found:
                if left_node is not None:
                    node = left_node
                elif right_node is not None:
                    node = right_node
                else:
                    node = root
        else:
            p_left_found, q_left_found, left_node = self.dfs(root.left, p, q) 
            p_right_found, q_right_found, right_node = self.dfs(root.right, p, q)
            p_found = p_left_found or p_right_found
            q_found = q_left_found or q_right_found
            if p_found and q_found:
                if left_node is not None:
                    node = left_node
                elif right_node is not None:
                    node = right_node
                else:
                    node = root
        return p_found, q_found, node

            