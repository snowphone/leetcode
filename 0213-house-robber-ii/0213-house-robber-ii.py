class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def fn(idx: int, beg, end):
            if idx < beg:
                return 0
            if idx in [beg, beg+1]:
                return nums[idx]
            return max(
                nums[idx] + fn(idx-2, beg, end), 
                nums[idx] + fn(idx-3, beg, end),
                fn(idx-1, beg, end),
            )
        
        if n <= 3:
            return max(nums)
        return max(
            fn(n-1, 1, n-1),
            fn(n-2, 0, n-2),
        )