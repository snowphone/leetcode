# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self, head):
        prev = ListNode(0, head)
        slow = head; fast = head
        while fast:
            prev, slow = slow, slow.next
            try:
                fast = fast.next.next
            except:
                break
        prev.next = None
        return slow
    
    def rev(self, head):
        prev = None
        nd = head
        while nd:
            nxt = nd.next
            nd.next = prev
            prev, nd = nd, nxt
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middle(head)
        revhead = self.rev(mid)
        dummy = ListNode(); tail = dummy

        while head and revhead:
            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = revhead
            tail = tail.next
            revhead = revhead.next

        if head:
            tail.next = head
    