class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sn = set(nums)
        return next(
            it for it in range(len(nums)+1) if it not in sn
        )