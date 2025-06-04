# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you actually want to take action when you are at even number
    # BFS
    # collect the value in list
    # pop node from queue but insert it again
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            if queue[0][1] % 2 == 1:
                self.reverse(queue)
            else:
                for i in range(len(queue)):
                    node, height = queue.popleft()
                    if node.left:
                        queue.append((node.left, height + 1))
                    if node.right:
                        queue.append((node.right, height + 1))
        return root

    def reverse(self, queue):
        nums = []
        for i in range(len(queue)):
            node, height = queue.popleft()
            nums.append(node.val)
            queue.append((node, height))
        j = len(nums) - 1
        #print(nums)
        for i in range(len(queue)):
            node, height = queue.popleft()
            node.val = nums[j]
            j -= 1
            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))
