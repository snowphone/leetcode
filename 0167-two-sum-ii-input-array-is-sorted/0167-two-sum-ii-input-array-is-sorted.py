from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        for i, it in enumerate(numbers):
            idx = bisect_left(numbers, target - it, lo=i+1)
            
            if not (i < idx < n and numbers[idx] == target - it):
                continue
            return [i+1, idx+1]
        