class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(i <= j for i, j in zip(nums, nums[1:])) or all(i >= j for i, j in zip(nums, nums[1:]))