class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        buffer = 1
        up = True
        for prev, it in zip(nums, nums[1:]):
            if prev < it:
                if up:
                    buffer += 1
                else:
                    buffer = 2
                up = True
            elif prev > it:
                if not up:
                    buffer += 1
                else:
                    buffer = 2
                up = False
            else:
                buffer = 0
            answer = max(answer, buffer)
        return answer
