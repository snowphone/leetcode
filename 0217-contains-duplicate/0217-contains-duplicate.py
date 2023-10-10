class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for it in nums:
            if it in cache:
                return True
            cache.add(it)
        return False