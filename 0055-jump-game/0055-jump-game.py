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
        return fn(0)