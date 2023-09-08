class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @cache
        def ncr(n, r):
            if n == 0 or r in [0, n]:
                return 1
            
            return ncr(n-1, r) + ncr(n-1, r-1)
        

        return [[ncr(n, r) for r in range(n + 1)]  for n in range(numRows)]