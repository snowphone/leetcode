class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def fn(i):
            if i >= n - 1:
                return 0
            
            if i + nums[i] >= n - 1:
                return 1

            return 1 + min(
                (
                    fn(j) 
                    for j in range(i+1, i+nums[i] + 1)
                ), default=987654321
             )

        return fn(0)

