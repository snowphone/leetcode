# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if bool(root) ^ bool(subRoot):
            return False
        
        def equals(lhs, rhs):
            if bool(lhs) ^ bool(rhs):
                return False
            if not lhs and not rhs:
                return True
            return lhs.val == rhs.val and equals(lhs.left, rhs.left) and equals(lhs.right, rhs.right)
        
        return equals(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
