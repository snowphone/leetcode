class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # 2 3 4 4 5 6
        
        nums.sort()
        
        n = len(nums)
        answer = 0
        for i in range(n // 2):
            answer = max(answer, nums[i] + nums[n - 1 - i])
        return answer