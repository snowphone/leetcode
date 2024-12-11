class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort() # This make the subsequence problem into the substring problem :)

        answer, l = 0, 0
        for r, rit in enumerate(nums):
            lit = lambda:  nums[l]
            while lit() + k < rit - k:
                l += 1
            answer = max(answer, r - l + 1)
        return answer