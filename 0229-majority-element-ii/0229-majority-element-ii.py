from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        a_third = len(nums) // 3

        return [
            it for it, c in cnt.items() if c > a_third
        ]
