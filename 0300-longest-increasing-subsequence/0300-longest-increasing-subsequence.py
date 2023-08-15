from functools import cache

class Solution:
    @cache
    def impl(self, idx: int):
        target = self.nums[idx]
        if(idx == 0):
            return 1;
        
        smallerOnes = [i for i in range(0, idx) if self.nums[i] < target]
        if not smallerOnes:
            return 1
        cand = [self.impl(i) for i in smallerOnes]
        return max(cand) + 1
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        inputs = list(range(len(nums)-1, -1, -1))
        return max([self.impl(i) for i in inputs])