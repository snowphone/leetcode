class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer, candidate = nums[0], 0

        for it in nums:
            candidate = max(candidate + it, it)
            answer = max(candidate, answer)

        return answer