class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        buffer = 1
        up = None
        for prev, it in zip(nums, nums[1:]):
            print(prev, it, up)
            if prev < it:
                if up is True:
                    buffer += 1
                else:
                    buffer = 2
                up = True
            elif prev > it:
                if up is False:
                    buffer += 1
                else:
                    buffer = 2
                up = False
            else:
                buffer = 0
                up = None
            answer = max(answer, buffer)
        return answer
