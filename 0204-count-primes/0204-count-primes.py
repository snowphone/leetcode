class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [False, False] + [True] * (n-2)

        for i, it in enumerate(nums):
            if not it:
                continue
            
            idx = i + i
            while idx < len(nums):
                nums[idx] = False
                idx += i
        
        return sum(nums)

        