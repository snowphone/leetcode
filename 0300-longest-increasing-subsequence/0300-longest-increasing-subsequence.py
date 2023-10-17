class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        "O(n^2) algorithm"
        @cache
        def fn(idx):
            if idx == 0:
                return 1
            
            it = nums[idx]
            answer = 0
            for i in range(idx):
                if nums[i] >= it:
                    continue
                answer = max(answer, fn(i))
            return answer + 1
        
        return max(fn(i) for i in range(len(nums)))
