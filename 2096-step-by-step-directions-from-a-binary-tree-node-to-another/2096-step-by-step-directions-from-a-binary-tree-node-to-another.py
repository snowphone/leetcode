from queue import SimpleQueue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _graphify(self, root, parent):
        if root.left:
            self._graphify(root.left, root)
        if root.right:
            self._graphify(root.right, root)
        
        root.parent = parent
        return root
    
    def _find(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self._find(root.left, val) or self._find(root.right, val)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = self._graphify(root, None)
        start = self._find(graph, startValue)

        q = SimpleQueue()
        q.put( (start, '') )
        visited = set([startValue])

        while not q.empty():
            nd, path = q.get()
            for nxt, action in [(nd.parent, 'U'), (nd.left, 'L'), (nd.right, 'R')]:
                if nxt is None or nxt.val in visited:
                    continue
                visited.add(nxt.val)
                if nxt.val == destValue:
                    return path + action
                
                q.put( (nxt, path + action) )
        return None