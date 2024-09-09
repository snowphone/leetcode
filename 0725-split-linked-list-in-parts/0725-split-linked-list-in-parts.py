# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _len(self, head):
        sz = 0
        while head:
            sz += 1
            head = head.next
        return sz
    
    def _calc_target_lengths(self, list_size: int, chunk_size: int):
        target_lengths = [list_size // chunk_size for _ in range(chunk_size)]
        for i in range(list_size - ( (list_size // chunk_size) * chunk_size) ):
            target_lengths[i] += 1

        return target_lengths
    
    def _take(self, head, n):
        dummy = ListNode(None, head)
        tail = dummy
        for _ in range(n):
            tail = tail.next

        new_head = tail.next
        tail.next = None

        return dummy.next, new_head

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sz = self._len(head)
        target_lengths = self._calc_target_lengths(sz, k)
        
        answer = []
        for chunk in target_lengths:
            it, head = self._take(head, chunk)
            answer.append(it)
        
        return answer
