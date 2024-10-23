from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        linesum = self._calc_linewise_sum(root, defaultdict(int), 1)
        self._modify(root, linesum, 1)
        root.val = 0
        return root
    
    def _modify(self, root, linesum, depth):
        children = [it for it in [root.left, root.right] if it]
        children_sum = sum(it.val for it in children)
        if root.left:
            root.left.val = linesum[depth+1] - children_sum
            self._modify(root.left, linesum, depth + 1)
        if root.right:
            root.right.val = linesum[depth+1] - children_sum
            self._modify(root.right, linesum, depth + 1)
        return

    def _calc_linewise_sum(self, root, acc, depth):
        acc[depth] += root.val
        root.left and self._calc_linewise_sum(root.left, acc, depth + 1)
        root.right and self._calc_linewise_sum(root.right, acc, depth + 1)
        return acc
