class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(
            (i&1) != (j&1) for i, j in zip(nums, nums[1:])
        )