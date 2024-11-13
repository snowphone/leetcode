from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        answer = 0
        for i, it in enumerate(nums):
            idx1 = bisect_left(nums, lower - it)
            idx2 = bisect_right(nums, upper - it)
            print(i, idx1, idx2)
            tmp = idx2 - idx1
            if idx1 <= i < idx2:
                tmp -= 1

            answer += tmp
        return answer // 2