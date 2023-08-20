# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 += l2
        answer = l1

        l1_prev, l2_prev = None, None
        carry = 0
        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode()
                l1_prev.next = l1
            if not l2:
                l2 = ListNode()
                l2_prev.next = l2
            
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10

            l1_prev, l1 = l1,  l1.next
            l2_prev, l2 = l2,  l2.next
        
        return answer

