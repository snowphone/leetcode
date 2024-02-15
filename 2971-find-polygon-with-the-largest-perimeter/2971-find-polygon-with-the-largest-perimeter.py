class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        answer = -1

        acc = 0
        for i, it in enumerate(nums):
            if i <= 1:
                acc += it
                continue
            if acc > it:
                answer = acc + it
            acc += it
        return answer