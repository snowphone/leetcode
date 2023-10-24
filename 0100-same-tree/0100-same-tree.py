# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p, q) == (None, None):
            return True
        
        TreeNode.__eq__ = lambda self, other: other is not None and self.val == other.val

        return p == q and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)