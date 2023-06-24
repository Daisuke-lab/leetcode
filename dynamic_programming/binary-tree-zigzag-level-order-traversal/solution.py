# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [{"node":root, "depth": 0}]
        answers = []
        current_depth = 0
        answer = []
        while len(queue) > 0:
            item = queue.pop(0)
            if item["node"] is None:
                continue
            if current_depth != item["depth"]:
                current_depth = item["depth"]
                if current_depth % 2 == 0:
                    answer = reversed(answer)
                answers.append(answer)
                answer = []


            answer.append(item["node"].val)
            
            queue.append({"node": item["node"].left, "depth": item["depth"] + 1})
            queue.append({"node": item["node"].right, "depth": item["depth"] + 1})

        if current_depth % 2 == 1:
            answer = reversed(answer)
        answers.append(answer)
        return answers
    