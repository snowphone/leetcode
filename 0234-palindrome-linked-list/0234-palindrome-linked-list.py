# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, nd):
        prev = None
        while nd:
            after = nd.next
            nd.next = prev
            prev, nd = nd, after
        return prev
    
    def middle(self, head):
        prev = None; slow = head; fast = head
        while fast:
            prev, slow = slow, slow.next
            try:
                fast = fast.next.next
            except:
                break
        prev.next = None
        return slow
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middle(head)
        rhs = self.rev(middle)
        lhs = head

        while lhs and rhs:
            if lhs.val != rhs.val:
                return False
            lhs = lhs.next
            rhs = rhs.next
        return True