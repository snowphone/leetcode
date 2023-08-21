# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        prev, nd = dummy_head, head

        while nd and nd.next:
            me = nd
            nxt = nd.next
            nxt_nxt = nxt.next

            prev.next = nxt
            nxt.next = me
            me.next = nxt_nxt

            prev, nd = me, nxt_nxt

        return dummy_head.next