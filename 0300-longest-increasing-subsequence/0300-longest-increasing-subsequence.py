from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = nums[:1]

        for it in nums[1:]:
            if ans and ans[-1] < it:
                ans.append(it)
            else:
                idx = bisect_left(ans, it)
                ans[idx] = it
        return len(ans)
