# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.bfs(root)


    def bfs(self, root):

        if root is None:
            return True
        queue = [{"height": 0, "node":root}]
        current_level = 0
        values = []
        while len(queue) > 0:
            current = queue.pop(0)
            current_height = current["height"]
            current_node = current["node"]

            if current_height > current_level:
                current_level = current_height
                values = []
            
            if len(values) == 0:
                if current_level % 2 == 1 and current_node.val % 2 == 0:
                    values.append(current_node.val)
                elif current_level % 2 == 0  and current_node.val % 2 == 1:
                    values.append(current_node.val)
                else:
                    return False

            else:
                if current_level % 2 == 1 and values[-1] > current_node.val and current_node.val % 2 == 0:
                    values.append(current_node.val)
                elif current_level % 2 == 0 and values[-1] < current_node.val and current_node.val % 2 == 1:
                    values.append(current_node.val)
                else:
                    return False
            if current_node.left is not None:
                queue.append({"height": current_height + 1, "node": current_node.left})

            if current_node.right is not None:
                queue.append({"height": current_height + 1, "node": current_node.right})
        return True