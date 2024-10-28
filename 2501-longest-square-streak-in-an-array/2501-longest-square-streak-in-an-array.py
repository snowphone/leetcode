class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numset = set(nums)
        sz = len(nums)

        @cache
        def solve(num):
            if num * num in numset:
                return 1 + solve(num*num)
            else:
                return 0
        
        answer = max( solve(it) for it in nums )
        if answer == 0:
            return -1
        return answer + 1
        