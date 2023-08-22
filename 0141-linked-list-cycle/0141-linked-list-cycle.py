# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while fast:
            if slow is fast:
                return True
            slow = slow.next
            try:
                fast = fast.next.next
            except:
                break
        return False