# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _record_parent(self, root, parent):
        if not root:
            return
        root.parent = parent
        root.id = id(root)
        self._record_parent(root.left, root)
        self._record_parent(root.right, root)
        return
    
    def traverse(self, start, available_step):
        answer = 0

        visited = set([start.id])
        q = [start]

        step = 0
        while q and step < available_step:
            next_q = []
            for nd in q:
                for nxt in [nd.parent, nd.left, nd.right]:
                    if nxt is None or nxt.id in visited:
                        continue
                    if nxt.id in self.leave_vals:
                        answer += 1
                    visited.add(nxt.id)
                    next_q.append(nxt)
            q = next_q
            step += 1

        return answer
    
    def leaves(self, root):
        answer = []
        if not root:
            return answer
        if not root.left and not root.right:
            answer.append(root)
        return answer + self.leaves(root.left) + self.leaves(root.right)

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self._record_parent(root, None)
        answer = 0

        leaves = self.leaves(root)
        self.leave_vals = set(it.id for it in leaves)

        for leaf in leaves:
            answer += self.traverse(leaf, distance)
        return answer // 2
