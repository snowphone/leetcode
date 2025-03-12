from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        num_negative = bisect_left(nums, 0)
        num_positive = len(nums) - bisect_right(nums, 0)

        return max(num_negative, num_positive)