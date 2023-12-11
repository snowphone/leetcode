class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        quarter = n // 4
        
        for i in range(quarter, n):
            if arr[i] == arr[i-quarter]:
                return arr[i]
        return None