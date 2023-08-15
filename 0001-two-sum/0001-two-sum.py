class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc = dict()
        for i, n in enumerate(nums):
            loc[n] = i

        for i, n in enumerate(nums):
            other = target - n
            if other not in loc:
                continue
            if n == other and i == loc[other]:
                continue
            return [i, loc[other]]
