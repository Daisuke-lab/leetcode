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
    private int low;
    private int high;
    public TreeNode trimBST(TreeNode root, int low, int high) {
        this.low = low;
        this.high = high;
        return trim(root);
    }
    
    public TreeNode trim(TreeNode node) {
        if (node == null) {
            return null;
        }
        if (node.val < low) {
            node = trim(node.right);
        } else if (node.val > high) {
            node = trim(node.left);
        } else{
            node.left = trim(node.left);
            node.right = trim(node.right);
        }
        return node;
    }
}