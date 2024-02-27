/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function dfs(root: TreeNode | null): [number, number] {
	if (!root) {
		return [0, 0]
	}
	const [left_d, left_l] = dfs(root.left)
	const [right_d, right_l] = dfs(root.right)
	const depth = 1 + Math.max(left_d, right_d)
	const length = Math.max(left_l, right_l, left_d + right_d)
	return [depth, length]
}

function diameterOfBinaryTree(root: TreeNode | null): number {
	return dfs(root)[1]
}