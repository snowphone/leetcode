class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        def find_top_idx():
            m = max(nums)
            return next(
                (i for i in range(n + 1) if nums[i % n] > nums[(i+1) % n]),
                0,
            )
        
        idx = find_top_idx()

        new_beg = idx + 1

        def at(idx: int):
            return nums[idx % n]

        return all(
            at(i) <= at(i+1)
            for i in range(new_beg, new_beg + n - 1)
        )

    