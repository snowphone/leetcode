# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.acc = 0

        def calc(nd):
            if not nd:
                return
            elif low <= nd.val <= high:
                self.acc += nd.val
                calc(nd.left)
                calc(nd.right)
            elif nd.val < low:
                calc(nd.right)
            elif high < nd.val:
                calc(nd.left)
            return
        
        calc(root)
        return self.acc