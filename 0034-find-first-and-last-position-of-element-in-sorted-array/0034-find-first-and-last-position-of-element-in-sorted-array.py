from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []
        l = bisect_left(nums, target)
        if 0 <= l < len(nums) and nums[l] == target:
            answer.append(l)
        else:
            answer.append(-1)

        r = bisect_right(nums, target)
        if 0 <= r-1 < len(nums) and nums[r-1] == target:
            answer.append(r-1)
        else:
            answer.append(-1)
        return answer
            
        