# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt_head, lt_tail = None, None
        other_head, other_tail = None, None

        nd = head

        while nd:
            if nd.val < x:
                if not lt_head:
                    lt_head, lt_tail = nd, nd
                else:
                    lt_tail.next = nd
                    lt_tail = lt_tail.next
            else:
                if not other_head:
                    other_head, other_tail = nd, nd
                else:
                    other_tail.next = nd
                    other_tail = other_tail.next
            nd = nd.next

        if other_tail:
            other_tail.next = None
        if lt_tail:
            lt_tail.next = other_head
            return lt_head
        else:
            return other_head
