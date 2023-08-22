# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nd = None, head
        while nd:
            after = nd.next
            nd.next = prev
            prev, nd = nd, after

        return prev