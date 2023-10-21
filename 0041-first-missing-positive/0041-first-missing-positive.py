class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = { it for it in nums if it > 0 }
        if not numset:
            return 1
        mini = min(numset)

        if mini > 1:
            return 1
        
        i = 1
        while True:
            if i not in numset:
                return i
            i += 1