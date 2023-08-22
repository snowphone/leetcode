# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def negate(self, head):
        nd = head
        while nd:
            nd.val = -nd.val
            nd = nd.next
        return

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        self.negate(headA)
        
        nd = headB
        answer = None
        while nd:
            if nd.val < 0:
                answer = nd
                break
            nd = nd.next
        self.negate(headA)

        return answer
        