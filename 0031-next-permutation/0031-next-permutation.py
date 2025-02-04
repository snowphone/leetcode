class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(b: int, e: int):
            while b < e:
                nums[b], nums[e - 1] = nums[e - 1], nums[b]
                b, e = b + 1, e - 1
            return

        try:
            i = next(i - 1 for i in range(n - 1, 0, -1) if nums[i - 1] < nums[i])
        except StopIteration:
            reverse(0, n)
            return

        it = nums[i]

        jt = min(jt for jt in nums[i + 1 :] if jt > it)
        j = next(j for j in range(n - 1, i, -1) if nums[j] == jt)

        nums[i], nums[j] = nums[j], nums[i]
        reverse(i + 1, n)
