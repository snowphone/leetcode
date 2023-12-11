class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        i = 0
        while i < n:
            j = next( (k for k in range(i, n) if arr[i] != arr[k]), n)
    
            if j - i > 0.25 * n:
                return arr[i]
            i = j
        