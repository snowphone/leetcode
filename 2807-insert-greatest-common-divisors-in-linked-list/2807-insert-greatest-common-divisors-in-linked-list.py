from math import gcd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _insert(self, it, val):
        'Insert new item just before `it` node and return the new node'
        new_item = ListNode(val, it)
        return new_item
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, it = head, head.next

        while it:
            print("prev, ME", prev.val, it.val)
            val = gcd(prev.val, it.val)
            prev.next = self._insert(it, val)
            prev, it = it, it.next

        return head
        