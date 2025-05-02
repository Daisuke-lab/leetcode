/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        return goodNodes(root, -(int) Math.pow(10, 4) -1);
    }

    public int goodNodes(TreeNode root, int maxScore) {
        if (root == null) {
            return 0;
        }
        int count = maxScore <= root.val ? 1 : 0;
        int newMaxScore = Math.max(maxScore, root.val);
        count += goodNodes(root.left, newMaxScore);
        count += goodNodes(root.right, newMaxScore);
        return count;
    }
}