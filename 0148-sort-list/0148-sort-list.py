# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _partition(self, head):
        prev = None
        one = head; two = head
        while one and two:
            prev, one = one, one.next
            try:
                two = two.next.next
            except:
                break
        prev.next = None
        return head, one
    
    def _merge(self, lhs, rhs):
        dummy = ListNode()
        tail = dummy
        while lhs and rhs:
            if lhs.val < rhs.val:
                tail.next = lhs
                lhs = lhs.next
            else:
                tail.next = rhs
                rhs = rhs.next
            tail = tail.next
        if not lhs:
            tail.next = rhs
        if not rhs:
            tail.next = lhs
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lhs, rhs = self._partition(head)
        lhs, rhs = map(self.sortList, [lhs, rhs])

        return self._merge(lhs, rhs)

