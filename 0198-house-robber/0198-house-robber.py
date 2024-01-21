class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def fn(i: int):
            if i >= len(nums):
                return 0
            return nums[i] + max(
                fn(i + 2),
                fn(i + 3),
            )
        return max(
            fn(0),
            fn(1),
        )