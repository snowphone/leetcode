class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        "Do not return anything, modify nums in-place instead."
        sz = len(nums)
        num_idx = 0
        for idx in range(sz):
            num_idx = max(idx, num_idx)
            
            if nums[idx] != 0:
                continue
            zero_idx = idx
            try:
                num_idx = next(i for i in range(num_idx, sz) if nums[i] != 0)
                nums[num_idx], nums[zero_idx] = nums[zero_idx], nums[num_idx]
            except StopIteration:
                break
        return
