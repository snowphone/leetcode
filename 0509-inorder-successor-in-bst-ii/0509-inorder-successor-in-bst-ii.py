"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        def goleft(root):
            if not root.left:
                return root
            return goleft(root.left)
        
        def goup(root):
            if not root:
                return None
            if node.val < root.val:
                return root
            return goup(root.parent)

        
        if node.right:
            return goleft(node.right)
        return goup(node.parent)