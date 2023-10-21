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
    public int sumNumbers(TreeNode root) {
        return dfs(root, new ArrayList<>()).stream().mapToInt(Integer::valueOf).sum();
    }

    private List<Integer> dfs(TreeNode root, List<String> digits) {
        digits.add(String.valueOf(root.val)) ;

        if (root.left == null && root.right == null) {
            var num = toInt(digits);
            digits.remove(digits.size() - 1);
            return List.of(num);
        }

        var answer = new ArrayList<Integer>();
        if (root.left != null) {
            answer.addAll(dfs(root.left, digits));
        }
        if (root.right != null) {
            answer.addAll(dfs(root.right, digits));
        }

        digits.remove(digits.size() - 1);
        return answer;
    }

    private int toInt(List<String> digits) {
        return Integer.parseInt(
                String.join("", digits)
        );
    }
}