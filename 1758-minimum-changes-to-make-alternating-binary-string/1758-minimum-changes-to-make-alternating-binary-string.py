class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        def diff(a, b):
            return sum(
                it != jt
                for it, jt in zip(a, b)
            )
        
        return min(
            diff(s, '10' * n),
            diff(s, '01' * n),
        )
