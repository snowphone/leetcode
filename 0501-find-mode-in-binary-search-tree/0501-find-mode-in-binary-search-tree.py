# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, acc):
            if not root:
                return acc
            dfs(root.left, acc)
            acc.append(root.val)
            dfs(root.right, acc)
            return acc
        

        nums = dfs(root, [])
        c = Counter(nums)
        maxcnt = max(c.values())

        return [k for k, v in c.items() if v == maxcnt]


        