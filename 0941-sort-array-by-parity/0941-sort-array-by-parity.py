class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0; j = len(nums) - 1
        while i < j:
            it  = nums[i]
            jt = nums[j]

            if it % 2 == 0:
                i += 1
                continue
            nums[i], nums[j] = jt, it

            j -= 1

        return nums