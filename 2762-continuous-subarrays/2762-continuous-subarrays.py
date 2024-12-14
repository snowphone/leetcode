from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        s = SortedList()
        l = 0
        lit = lambda: nums[l]
        answer = 0
        for r, rit in enumerate(nums):
            s.add(rit)
            while s and s[-1] - s[0] > 2:
                s.remove(lit())
                l += 1
            answer += len(s)

        return answer

