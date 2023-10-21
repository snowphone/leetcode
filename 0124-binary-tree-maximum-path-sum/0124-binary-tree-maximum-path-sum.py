# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -987654321

        def dfs(root: TreeNode):
            if not root.left and not root.right:
                self.answer = max(self.answer, root.val)
                return root.val
            
            left = dfs(root.left) if root.left else -987654321
            right = dfs(root.right) if root.right else -987654321

            self.answer = max(self.answer, left + root.val, right + root.val, left + right + root.val, root.val)
            return root.val + max(left, right, 0)

        dfs(root)
        return self.answer