# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.equals(root.left, root.right)

    def equals(self, lhs, rhs):
        if not lhs and not rhs:
            return True
        elif lhs and rhs:
            return (
                lhs.val == rhs.val and 
                self.equals(lhs.right, rhs.left) and 
                self.equals(lhs.left, rhs.right)
            )
        return False