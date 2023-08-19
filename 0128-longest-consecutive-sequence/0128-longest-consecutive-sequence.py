class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()

        cnt = 1
        answer = 1
        for n, m in zip(nums, nums[1:]):
            if n + 1 == m:
                cnt += 1
            elif n == m:
                continue
            else:
                cnt = 1
            answer = max(answer, cnt)
        return answer
