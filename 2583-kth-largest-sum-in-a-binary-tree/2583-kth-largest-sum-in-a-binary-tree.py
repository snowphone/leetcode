# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.sum = defaultdict(int)
        self._acc(root, 1)

        if k > len(self.sum):
            return -1
        return sorted(self.sum.values(), reverse=True)[k-1]
    
    def _acc(self, root: TreeNode | None, depth: int):
        self.sum[depth] += root.val
        root.left and self._acc(root.left, depth + 1)
        root.right and self._acc(root.right, depth + 1)
        return
        