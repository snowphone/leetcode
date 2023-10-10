class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        cache = set()
        for j in range(n):
            it = nums[j]
            if it in cache:
                return True
            
            cache.add(it)
            while j - i + 1 > k:
                cache.remove(nums[i])
                i += 1

        return False