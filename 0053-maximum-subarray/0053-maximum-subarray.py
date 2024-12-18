class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]

        candidate = nums[0]
        for it in nums[1:]:
            candidate = max(candidate + it, it)
            answer = max(candidate, answer)

        return answer