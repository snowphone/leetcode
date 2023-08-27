from operator import mul
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeronum = nums.count(0)

        if zeronum > 1:
            return [0] * len(nums)
        elif zeronum == 1:
            acc = reduce(mul, (it for it in nums if it != 0) )
            return [acc if it == 0 else 0 for it in nums]
        else:
            acc = reduce(mul, (it for it in nums if it != 0) )
            return [acc // it for it in nums]
