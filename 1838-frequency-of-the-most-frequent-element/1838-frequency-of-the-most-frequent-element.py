class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        answer = 0
        acc = 0
        for r in range(len(nums)):
            it = nums[r]
            acc += it
            while l < r and (r - l + 1) * it - acc > k:
                acc -= nums[l]
                l += 1
            answer = max(answer, r - l + 1)

        return answer