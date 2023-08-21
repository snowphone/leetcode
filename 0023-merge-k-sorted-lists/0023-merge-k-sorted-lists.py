# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head

        lists = deque(it for it in lists if it)

        while lists:
            i = min(range(len(lists)), key=lambda idx: lists[idx].val)
            nd = lists[i]

            tail.next = nd
            tail = tail.next

            lists[i] = nd.next

            if not lists[i]:
                del lists[i]

        return dummy_head.next