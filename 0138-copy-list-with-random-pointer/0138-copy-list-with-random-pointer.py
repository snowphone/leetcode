"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = dict()

        dummy = Node(0)
        tail = dummy

        while head:
            if head not in cache:
                cache[head] = Node(head.val, head.next, head.random)
            copied = cache[head]

            nxt = copied.next
            if nxt not in cache:
                cache[nxt] =  Node(nxt.val, nxt.next, nxt.random) if nxt else None
            copied.next = cache[nxt]

            rd = copied.random
            if rd not in cache:
                cache[rd] = Node(rd.val, rd.next, rd.random) if rd else None
            copied.random = cache[rd]

            tail.next = copied
            tail = tail.next
            head = head.next

        return dummy.next