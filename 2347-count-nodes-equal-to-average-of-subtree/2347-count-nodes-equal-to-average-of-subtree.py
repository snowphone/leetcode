# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def precalc(root):
            "Calculate sum and cnt"
            if not root:
                return 0, 0

            leftsum, leftcnt = precalc(root.left)
            rightsum, rightcnt = precalc(root.right)

            root.sum = leftsum + rightsum + root.val
            root.cnt = leftcnt + rightcnt + 1

            return root.sum, root.cnt
        
        precalc(root)

        def dfs(root):
            if not root:
                return 0
            
            answer = 0
            if root.sum // root.cnt == root.val:
                answer += 1
            
            answer += dfs(root.left)
            answer += dfs(root.right)

            return answer
        
        return dfs(root)
