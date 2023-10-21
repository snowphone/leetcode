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
    private int answer = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return this.answer;
    }

    /**
     * 
     * @param root
     * @return Maximum path which contains its root
     */
    private int dfs(TreeNode root) {
        if (root == null) {
            return -987654321;
        }
        if (root.left == null && root.right == null) {
            answer = Math.max(answer, root.val);
            return root.val;
        }
        var left = dfs(root.left);
        var right = dfs(root.right);
        answer = IntStream.of(
                answer,
                left + root.val,
                right + root.val,
                left + right + root.val,
                root.val
        ).max().getAsInt();
        
        return root.val + IntStream.of(left, right, 0).max().getAsInt();
    }
}