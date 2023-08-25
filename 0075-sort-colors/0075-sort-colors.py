from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt = Counter(nums)
        nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]
