# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # you need to propage maxPathSum and maxPath as a half of path
    # When it comes to maxPath, the current is going to be joint, and then add left + right + curr
    # as the output, maxSum = max(leftMaxPathSum, rightMaxPathSum, currentMaxPathSum)
    # ast the output, maxPath = max(leftPath, rightPath) + current
    # because the output is different you need another function 
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]        

    def dfs(self, root):
        if root is None:
            return -float("inf"), -float("inf")
        else:
            left_max_path_sum, left_max_path = self.dfs(root.left)
            right_max_path_sum, right_max_path = self.dfs(root.right)
            result_max_path_sum = self.get_result_max_path_sum(left_max_path_sum, left_max_path, right_max_path_sum, right_max_path, root)
            result_max_path = self.get_result_max_path(left_max_path, right_max_path, root)
            return result_max_path_sum, result_max_path

    def get_result_max_path(self, left_max_path, right_max_path, root):
        return max(left_max_path, right_max_path) + root.val if max(left_max_path, right_max_path) > 0 else root.val

    def get_result_max_path_sum(self, left_max_path_sum, left_max_path,right_max_path_sum, right_max_path, root):
        paths = [left_max_path_sum, right_max_path_sum, root.val]
        curr_max_path_sum = left_max_path + right_max_path + root.val
        left_joint_path = left_max_path + root.val
        right_joint_path = right_max_path + root.val
        paths.append(curr_max_path_sum)
        paths.append(left_joint_path)
        paths.append(right_joint_path)
        return max(paths)
