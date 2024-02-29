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

function bfs(root: TreeNode): Array<Array<number>> {
	let q = [root]
	let answer: Array<Array<number>> = []

	while (q.length > 0) {
		const next_q = new Array<TreeNode>()
		answer.push([])

		for (const it of q) {
			answer[answer.length - 1].push(it.val)
			if (!!it.left) {next_q.push(it.left)}
			if (!!it.right) {next_q.push(it.right)}
		}
		q = next_q
	}

	return answer
}

function is_evenodd(levels: number[][]): boolean {
	for (let i = 0; i < levels.length; i++) {
		const op: (l: number, r: number) => boolean =
			(i & 1) ?
				(l, r) => l > r :
				(l, r) => l < r
		const values = levels[i]

		if (!values.every(it => !!(i & 1) !== !!(it & 1))) {
			return false
		}

		for (let j = 0; j < values.length - 1; ++j) {
			if (!op(values[j], values[j + 1])) {
				return false
			}
		}
	}
	return true
}

function isEvenOddTree(root: TreeNode): boolean {
	const levels = bfs(root)
	return is_evenodd(levels)
};