class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        buf = 0

        for it in nums:
            buf = max(buf + it, it)
            answer = max(buf, answer)
        return answer