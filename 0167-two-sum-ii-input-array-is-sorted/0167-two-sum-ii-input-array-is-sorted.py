from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n-1
        while i < j:
            if (acc := numbers[i] + numbers[j]) < target:
                i += 1
            elif acc > target:
                j -= 1
            else:
                return [i+1, j+1]
