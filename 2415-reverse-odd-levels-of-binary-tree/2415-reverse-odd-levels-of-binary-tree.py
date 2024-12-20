# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def to_2d_matrix(root: TreeNode | None):
            buffer = []
            q = [root]
            while q:
                buffer.append(q)
                new_q = []
                for it in q:
                    if not it:
                        break
                    new_q += [it.left, it.right]
                q = new_q
            return buffer

        def restruct_with_biennial_swap(buffer: list[list[TreeNode | None]]):
            for i in range(0, len(buffer) - 1):
                parents = buffer[i]
                children = buffer[i + 1]
                if i % 2 == 0:
                    children.reverse()
                for j, parent in enumerate(parents):
                    parent.left = children[j * 2]
                    parent.right = children[j * 2 + 1]
            return buffer[0][0]

        buffer = to_2d_matrix(root)
        return restruct_with_biennial_swap(buffer)
