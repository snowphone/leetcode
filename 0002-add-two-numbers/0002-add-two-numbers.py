# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def read(self, head):
        nd = head
        answer = []
        while nd:
            answer.append(str(nd.val))
            nd = nd.next
        return int("".join(reversed(answer)))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        nd, tail = None, None
        for n in reversed(str( self.read(l1) + self.read(l2) )) :
            if nd is None:
                nd = ListNode(n)
                tail = nd
            else:
                tail.next = ListNode(n)
                tail = tail.next
        return nd

