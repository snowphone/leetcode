class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def fn(i: int):
            if i == 0:
                return 1

            return 1 + max(
                (fn(j) for j, it in enumerate(nums[:i]) if it < nums[i]), default=0
            )
        
        return max(
            fn(i) for i in range(len(nums))
        )