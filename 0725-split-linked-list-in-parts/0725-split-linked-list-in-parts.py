# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self, head: Optional[ListNode]) -> int:
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt
    
    def take(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        for _ in range(n):
            tail = tail.next

        next_head = tail.next
        tail.next = None

        return dummy.next, next_head

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sz = self.len(head)
        answer = [None for _ in range(k)]
        remaining = sz % k

        for i in range(k):
            length = sz // k
            if remaining:
                length += 1
                remaining -= 1
            answer[i], head = self.take(head, length)

        return answer