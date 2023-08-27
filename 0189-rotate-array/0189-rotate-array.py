class Solution:
    def rev(self, nums, b, e):
        while b < e:
            nums[b], nums[e-1] = nums[e-1], nums[b]
            b += 1
            e -= 1
        return

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        self.rev(nums, 0, len(nums))
        self.rev(nums, 0, k)
        self.rev(nums, k, len(nums))