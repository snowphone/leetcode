class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        @cache
        def step(n: int):
            if n not in numset:
                return 0
            return 1 + step(n + 1)
        
        return max( (step(i) for i in numset), default=0)
