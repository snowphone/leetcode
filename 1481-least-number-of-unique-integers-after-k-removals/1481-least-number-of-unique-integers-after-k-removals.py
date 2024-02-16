class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = sorted(
            (it for it in Counter(arr).items()),
            key=lambda pair: pair[1],
        )

        idx = 0
        while k:
            it, cnt = nums[idx]
            if k >= cnt:
                k -= cnt
                idx += 1
                continue
            # Invariant: `it` is alive
            break

        return len(nums) - idx
            