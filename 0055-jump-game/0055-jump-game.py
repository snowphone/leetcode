class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n  = len(nums)

        @cache
        def fn(i: int):
            if i >= n - 1:
                return True
            
            if i + nums[i] >= n - 1:
                return True
            

            return any(
                fn(j) for j in range(i+1, i + nums[i] + 1)
            )
        for i in range(n-1, 0, -1):
            fn(i)  # Warm up cache
            
        return fn(0)