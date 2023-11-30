
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        @cache
        def solve_2k(n):
            return {
                n: lambda: 2 * solve_2k(n//2) + 1,
                0: lambda: 0,
                1: lambda: 1,
            }[n]()
        
        acc = []
        for i in range(31, -1, -1):
            if n & (1 << i):
                acc.append( solve_2k(1 << i) )
            
        return sum(acc[::2]) - sum(acc[1::2])
            
