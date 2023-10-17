class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def fn(target: int):
            if target == 0:
                return 1
            if target < 0:
                return 0
            answer = 0
            for i, it in enumerate(nums):
                answer += fn(target - it)
            return answer
        
        return fn(target)