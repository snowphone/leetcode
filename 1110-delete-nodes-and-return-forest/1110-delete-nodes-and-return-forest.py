# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _record_parents(self, root, parent):
        parents = { root.val: parent } 
        
        if root.left:
            parents |= self._record_parents(root.left, root)
        if root.right:
            parents |= self._record_parents(root.right, root)

        return parents
    
    def _record_val_to_node(self, root):
        mapping = {}
        if root:
            mapping[root.val] = root
            mapping |= self._record_val_to_node(root.left)
            mapping |= self._record_val_to_node(root.right)
        return mapping

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        parents = self._record_parents(root, None)
        mapping = self._record_val_to_node(root)

        for to_del_val in to_delete:
            nd = mapping[to_del_val]

            parent = parents[to_del_val]
            if parent and parent.left and parent.left.val == to_del_val:
                parent.left = None
            if parent and parent.right and parent.right.val == to_del_val:
                parent.right = None

            l = nd.left
            r = nd.right
            if l:
                parents[l.val] = None
            if r:
                parents[r.val] = None
        
        existing_nodes = set(mapping.keys()) - set(to_delete)
        return [ mapping[it] for it in existing_nodes if not parents[it] ]