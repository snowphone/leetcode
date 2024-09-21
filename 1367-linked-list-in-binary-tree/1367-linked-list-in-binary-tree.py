# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        for it in self._find_all(root, head.val):
            print("TRY")
            if self._equals(head, it):
                return True
        return False
        
    def _equals(self, head, root):
        if not head:
            return True
        if head and not root:
            return False
        return (head.val == root.val) and (
            self._equals(head.next, root.left) or
            self._equals(head.next, root.right)
        )

    def _find_all(self, root: TreeNode|None, val: int):
        if not root:
            return
        if root.val == val:
            yield root
        
        # Both ways are equivalent.
        for it in self._find_all(root.left, val):
            yield it
        yield from self._find_all(root.right, val)