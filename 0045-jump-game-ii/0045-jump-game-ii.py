from functools import cache

class Solution:
    def jump(self, nums: List[int], idx: int = 0) -> int:
        n = len(nums)

        @cache
        def _jmp(i: int) -> int:
            if i == n - 1:
                return 0
    
            begin = i + 1
            end =  min(i + nums[i] + 1, n)
            if begin >= end:
                return n * n
    
            dst = range(end - 1, begin - 1, -1)
            return min(_jmp(it) for it in dst) + 1

        return _jmp(0)

