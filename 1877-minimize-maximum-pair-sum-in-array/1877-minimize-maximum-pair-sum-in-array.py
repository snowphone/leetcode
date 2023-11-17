class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        answer = 0
        for i in range(n // 2):
            answer = max(answer, nums[i] + nums[n - 1 - i])
        return answer