from functools import reduce
from operator import mul


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        prod = lambda iter: reduce(mul, iter)
        nums.sort()


        return prod(nums[-2:]) - prod(nums[:2])