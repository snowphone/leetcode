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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return root != null && dfs(root, targetSum);
    }
    private boolean dfs(TreeNode root, int target) {
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null && root.val == target) {
            return true;
        }
        return dfs(root.left, target - root.val) || dfs(root.right, target - root.val);
    }
}