class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        max_so_far = 1
        min_so_far = 1
        
        for it in nums:
            new_max_so_far = max(it, max_so_far * it, min_so_far * it)
            new_min_so_far = min(it, max_so_far * it, min_so_far * it)

            max_so_far, min_so_far = new_max_so_far, new_min_so_far
            answer = max(answer, max_so_far)
        return answer