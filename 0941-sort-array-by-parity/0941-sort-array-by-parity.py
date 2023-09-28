class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [it for it in nums if it % 2 == 0] + [it for it in nums if it % 2 != 0]