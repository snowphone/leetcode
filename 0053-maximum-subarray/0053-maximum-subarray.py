class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        max_so_far = 0
        
        for it in nums:
            max_so_far = max(it, it + max_so_far)
            answer = max(answer, max_so_far)
        return answer