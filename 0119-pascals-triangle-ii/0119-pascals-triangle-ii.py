from functools import cache

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        @cache
        def ncr(n, r):
            if n == 0:
                return 1
            if r in [0, n]:
                return 1
            return ncr(n-1, r) + ncr(n-1, r-1)
        
        return [ncr(rowIndex, r) for r in range(rowIndex + 1)]