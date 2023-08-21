# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda me, you: me.val < you.val

        dummy_head = ListNode()
        tail = dummy_head

        cnt = sum(1 for it in lists if it)
        q = PriorityQueue()
        for it in filter(None, lists):
            q.put(it)

        while not q.empty():
            nd = q.get()

            tail.next = nd
            tail = tail.next

            if nd.next:
                q.put(nd.next)
            
        return dummy_head.next