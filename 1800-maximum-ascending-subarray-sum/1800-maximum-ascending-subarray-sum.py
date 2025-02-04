class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        buf = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                buf += nums[i]
            else:
                buf = nums[i]
            answer = max(answer, buf)
        return answer