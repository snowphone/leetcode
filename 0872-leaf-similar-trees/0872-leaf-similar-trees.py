# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leaves(root, answer):
            if root.left:
                leaves(root.left, answer)
            if not root.left and not root.right:
                answer.append(root.val)
            
            if root.right:
                leaves(root.right, answer)
            return answer
        
        return leaves(root1, []) == leaves(root2, [])
        