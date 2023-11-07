class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [True] * n
        nums[0] = False
        nums[1] = False

        for i, it in enumerate(nums):
            if not it:
                continue
            
            idx = i + i
            while idx < len(nums):
                nums[idx] = False
                idx += i
        
        return nums.count(True)

        