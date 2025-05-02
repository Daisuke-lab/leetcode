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
    public boolean isBalanced(TreeNode root) {
        return recursion(root).getValue();
    }

    public Pair<Integer, Boolean> recursion(TreeNode root) {
        if (root == null) {
            return new Pair<>(0, true);
        }
        Pair<Integer, Boolean> leftPair = recursion(root.left);
        Pair<Integer, Boolean> rightPair = recursion(root.right);
        if (!leftPair.getValue() || !rightPair.getValue()) {
            return new Pair<>(0, false);
        }
        boolean valid = Math.abs(leftPair.getKey() - rightPair.getKey()) <= 1;
        int height = Math.max(leftPair.getKey(), rightPair.getKey()) + 1;
        return new Pair<>(height, valid);
    }
}