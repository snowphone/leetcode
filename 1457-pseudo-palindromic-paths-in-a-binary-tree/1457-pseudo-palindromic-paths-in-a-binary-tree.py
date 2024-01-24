# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Prerequisites for pseudo-palindrome:
        #   1. Odd frequency exists at most once.

        def is_pseudo_palindrome(counter: list[int]):
            odds = sum(1 for it in counter if it & 1)
            return int(odds <= 1)

        def dfs(root: TreeNode, counter: list[int]):
            counter[root.val] += 1
            answer = 0
            if not root.left and not root.right:
                answer += is_pseudo_palindrome(counter)
            if root.left:
                answer += dfs(root.left, counter)
            if root.right:
                answer += dfs(root.right, counter)
            counter[root.val] -= 1
            return answer
        
        return dfs(root, [0 for _ in range(10)])
            
