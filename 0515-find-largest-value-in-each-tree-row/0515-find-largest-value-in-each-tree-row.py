# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        answer = []
        q = [root]

        while q:
            new_q = []
            subanswer = -2 ** 31

            for it in q:
                subanswer = max(subanswer, it.val)
                if it.left:
                    new_q.append(it.left)
                if it.right:
                    new_q.append(it.right)

            answer.append(subanswer)
            q = new_q
        return answer