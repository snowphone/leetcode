class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        acc = 0
        for i in range(n + 1):
            acc ^= i
        for it in nums:
            acc ^= it
        return acc
