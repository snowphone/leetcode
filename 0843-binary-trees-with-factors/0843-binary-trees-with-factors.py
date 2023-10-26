from bisect import bisect_left
from functools import cache

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()

        @cache
        def fn(idx: int):
            if idx == 0:
                return 1
            n = arr[idx]
            answer = 1  # Myself
            indices = set()
            for i in range(idx):
                it = arr[i]
                if n % it:
                    continue
                j = bisect_left(arr, n // it, hi=idx)
                if not (0 <= j < idx) or arr[j] != n // it:
                    continue
                
                indices.add( (i, j) )
            
            for i, j in indices:
                # Append combinations of posssible children
                answer += (fn(i) * fn(j))

            return answer % (10 ** 9 + 7)
        
        return sum(fn(i) for i in range(len(arr))) % (10 ** 9 + 7)
                
            