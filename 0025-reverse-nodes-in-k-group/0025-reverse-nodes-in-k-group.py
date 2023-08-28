# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, k):
        '''
        If len(head) >= k, reverse the first `k` nodes and
        return (reversed head, reversed tail, next head).
        Otherwise, return (head, None, None).
        '''
        # Check whether the length is enough to reverse
        nd = head
        for _ in range(k):
            if not nd:
                return head, None, None
            nd = nd.next
        
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
        it = head

        while it:
            reversed_head, reversed_tail, new_head = self.reverse(it, k)
            tail.next = reversed_head
            tail = reversed_tail
            it = new_head
            
        return dummy_head.next