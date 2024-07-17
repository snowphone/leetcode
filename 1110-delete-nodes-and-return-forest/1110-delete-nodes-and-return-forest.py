# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _traverse(self, root, parent):
        answer = []
        if root.left:
            answer += self._traverse(root.left, root)
        if root.right:
            answer += self._traverse(root.right, root)
        
        if root.val in self.to_delete:
            answer += [it for it in [root.left, root.right] if it]

            if parent and parent.left and parent.left.val == root.val:
                parent.left = None
            if parent and parent.right and parent.right.val == root.val:
                parent.right = None

        return answer

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)

        answer = self._traverse(root, None)
        if root.val not in self.to_delete:
            answer.append(root)
        return answer


