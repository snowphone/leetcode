# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, acc):
            if not root.left and not root.right:
                acc.append(str(root.val))
                tmp = [int(''.join(acc))]
                acc.pop()
                return tmp
            
            acc.append(str(root.val))
            answer = []
            if root.left:
                answer += dfs(root.left, acc)
            if root.right:
                answer += dfs(root.right, acc)
            acc.pop()

            return answer
        
        return sum(dfs(root, []))
        