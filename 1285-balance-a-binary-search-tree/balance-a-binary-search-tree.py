# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # collect number 
    # pick median 
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nums = self.collect_nums(root, [])
        return self.build_tree(0, len(self.nums) -1)
    
    def build_tree(self, i, j):
        if i > j:
            return None
        if i == j:
            node = TreeNode(self.nums[i])
            return node
        m = (i + j) // 2
        node = TreeNode(self.nums[m])
        node.left = self.build_tree(i,m- 1)
        node.right = self.build_tree(m+1, j)
        return node

    def collect_nums(self, root, nums):
        if root is None:
            return nums
        self.collect_nums(root.left, nums)
        nums.append(root.val)
        self.collect_nums(root.right, nums)
        return nums
