from itertools import cycle

class Solution:
    def minOperations(self, s: str) -> int:
        def diff(a, b):
            return sum(
                it != jt
                for it, jt in zip(a, b)
            )
        
        return min(
            diff(s, cycle("01")),
            diff(s, cycle("10")),
        )
