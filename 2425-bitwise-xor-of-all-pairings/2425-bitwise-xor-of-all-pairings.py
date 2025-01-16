from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        if num2 even -> ignore nums1
        if 
        '''

        sum = lambda iter: reduce(operator.xor, iter)

        if len(nums2) & 1:
            lhs = sum(nums1)
        else:
            lhs = 0

        if len(nums1) & 1:
            rhs = sum(nums2)
        else:
            rhs = 0
            
        return lhs ^ rhs
        