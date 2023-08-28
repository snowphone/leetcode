# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, k):
        'Return [reversed head, reversed tail, next head]'
        # Check whether the length is enough to reverse
        _nd = head
        for _ in range(k):
            if not _nd:
                return head, None, None
            _nd = _nd.next
        
        # Reverse first `k` nodes
        prev, nd = None, head
        for _ in range(k):
            nxt = nd.next
            nd.next = prev
            prev, nd = nd, nxt

        return prev, head, nxt

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        tail = dummy_head
        nd = head

        while nd:
            reversed_head, reversed_tail, new_head = self.reverse(nd, k)
            tail.next = reversed_head
            tail = reversed_tail
            nd = new_head
            
        return dummy_head.next