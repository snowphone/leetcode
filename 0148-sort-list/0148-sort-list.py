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
        while lhs or rhs:
            if not lhs:
                tail.next = rhs
                break
            if not rhs:
                tail.next = lhs
                break
            if lhs.val < rhs.val:
                tail.next = lhs
                tail = tail.next
                lhs = lhs.next
            else:
                tail.next = rhs
                tail = tail.next
                rhs = rhs.next
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        one, two = self._partition(head)
        one = self.sortList(one)
        two = self.sortList(two)

        return self._merge(one, two)

