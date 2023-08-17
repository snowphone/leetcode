from operator import attrgetter
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lists = [list1, list2]
        self.patch()

        head = None
        tail = None

        pq = PriorityQueue()
        self.pq = pq

        for it in filter(None, lists):
            pq.put( it )

        while pq.qsize():
            it = self.pq.get()
    
            nxt = it.next
            if nxt:
                self.pq.put(nxt)
            it.next = None

            if not head:
                head = it
                tail = it
                continue

            tail.next = it
            tail = it
        return head
    
    @staticmethod
    def patch():
        def lt(self, other):
            return self.val < other.val
        ListNode.__lt__ = lt

        return
    