"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        if not root:
            return answer
        
        for child in root.children:
            answer += self.postorder(child)
        
        answer.append(root.val)
        return answer
        