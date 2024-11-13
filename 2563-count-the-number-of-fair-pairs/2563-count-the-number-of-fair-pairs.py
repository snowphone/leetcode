from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        answer = 0
        for i, it in enumerate(nums):
            idx1 = bisect_left(nums, lower - it)
            idx2 = bisect_right(nums, upper - it)

            if idx1 <= i < idx2:
                answer += (idx2 - idx1 - 1)
            else:
                answer += (idx2 - idx1)
        return answer // 2