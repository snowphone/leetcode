from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        answer = 10**9 + 1
        for b, it in enumerate(nums):
            last = it + n - 1

            e = bisect_right(nums, last)
            answer = min(answer, n - (e - b) )
        return answer
            
