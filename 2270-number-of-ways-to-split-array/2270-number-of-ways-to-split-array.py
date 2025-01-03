class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lsum = 0
        rsum = sum(nums)

        answer = 0
        for i, it in enumerate(nums):
            if i == len(nums) - 1:
                break
            lsum += it
            rsum -= it
            if lsum >= rsum:
                answer += 1
        return answer