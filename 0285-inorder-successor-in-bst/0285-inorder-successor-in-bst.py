# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.next = False

        def dfs(root):
            if not root:
                return None
            tmp = dfs(root.left)
            if tmp:
                return tmp

            if self.next:
                return root

            if root.val == p.val:
                self.next = True
            
            return dfs(root.right)
        
        return dfs(root)
