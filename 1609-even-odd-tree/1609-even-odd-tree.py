# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        q = [(0, root)]
        levels = defaultdict(list)
        while q:
            next_q = []
            for lv, it in q:
                levels[lv].append(it.val)
                if it.left: next_q.append((lv + 1, it.left))
                if it.right: next_q.append((lv + 1, it.right))
            q = next_q
        return levels
    
    def evenodd(self, lv, values):
        if lv & 1:  # decrease
            return all(it % 2 == 0 for it in values) and all(
                it > jt for it, jt in zip(values, values[1:])
            )
        else:  # increase
            return all(it & 1 for it in values) and all(
                it < jt for it, jt in zip(values, values[1:])
            )
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = self.bfs(root)

        return all(
            self.evenodd(lv, values) for lv, values in levels.items()
        )
