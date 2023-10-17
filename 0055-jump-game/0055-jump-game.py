class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def fn(idx: int):
            if idx == len(nums) - 1:
                return True
            if idx >= len(nums):
                return False

            n = nums[idx]
            return any(fn(i) for i in range(idx + n, idx, -1) )

        return fn(0)