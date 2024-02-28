# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        prev_q = None
        q = [root] if root else []

        while q:
            next_q = []
            for it in q:
                if it.left:
                    next_q.append(it.left)
                if it.right:
                    next_q.append(it.right)
            prev_q, q = q, next_q
        return prev_q

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)[0].val

        