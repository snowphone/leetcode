class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def fn(idx: int):
            if idx < 0:
                return 0
            if idx in [0, 1]:
                return nums[idx]
            
            return nums[idx] + max(fn(idx - 2), fn(idx - 3))

            return
        return max(
            fn(len(nums) - 1),
            fn(len(nums) - 2),
        )
