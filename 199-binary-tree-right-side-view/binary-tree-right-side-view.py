# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # when it's zig zag, it's hard
        # always choose right
        # when you can not choose right, you can go to left
        # bfs (queue) is more intuitive
        # you want to maintain the depth
        # if it's already added, you will not add to answer
        # but you need to add children to stack
        if root is None:
            return []
        answer = []
        queue = collections.deque()
        queue.append((root, 0))
        depths = set()
        while queue:
            node, depth = queue.popleft()
            if depth not in depths:
                depths.add(depth)
                answer.append(node.val)
            if node.right:
                queue.append((node.right, depth+1))
            if node.left:
                queue.append((node.left, depth+1))
        return answer
    
        