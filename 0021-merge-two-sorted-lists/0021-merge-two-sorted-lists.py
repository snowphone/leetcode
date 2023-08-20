# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # dummy node
        tail = head

        while list1 or list2:
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break
            if list1.val < list2.val:
                nd = list1
                list1 = list1.next
            else:
                nd = list2
                list2 = list2.next
            tail.next = nd
            tail = tail.next
        return head.next

