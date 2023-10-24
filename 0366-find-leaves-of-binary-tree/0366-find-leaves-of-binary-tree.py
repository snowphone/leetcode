# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(root, acc):
            if not root.left and not root.right:
                acc.append(root.val)
                return None
            
            if root.left:
                root.left = dfs(root.left, acc)
            if root.right:
                root.right = dfs(root.right, acc)

            return root
        answer = []
        line = []
        new_root = dfs(root, line)
        answer.append(line)

        if not new_root:
            return answer
        answer += self.findLeaves(new_root)
        return answer
        