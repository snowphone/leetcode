# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 0, 0  # depth, length

        left_d, left_l = self.dfs(root.left) if root.left else (0, 0)
        right_d, right_l = self.dfs(root.right) if root.right else (0, 0)
        
        dep = 1 + max(left_d, right_d)
        length = max(left_l, right_l, left_d + right_d)
        return dep, length
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]