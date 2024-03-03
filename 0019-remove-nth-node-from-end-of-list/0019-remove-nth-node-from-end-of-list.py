# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, root):
        sz = 0
        while root:
            sz += 1
            root = root.next
        return sz
    
    def remove(self, head, n):
        dummy = ListNode(val=-1, next=head)
        prev, it = dummy, head

        for _ in range(n):
            prev, it = it, it.next
        prev.next = it.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = self.len(head)
        n = sz - n  # 0-indexed

        return self.remove(head, n)
        