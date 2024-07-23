# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodemap = {}
        nodes = set()
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in nodemap:
                nodemap[parent] = TreeNode(parent)
            if child not in nodemap:
                nodemap[child] = TreeNode(child)
            
            nodes |= {parent, child}
            children.add(child)
            
            if is_left:
                nodemap[parent].left = nodemap[child]
            else:
                nodemap[parent].right = nodemap[child]
        
        root = next(it for it in nodes - children)
        return nodemap[root]
            