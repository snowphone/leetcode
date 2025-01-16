from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        nums1 = [a, b]
        nums2 = [1,2,3]
        cartesian xor = [a1, a2, a3, b1, b2, b3]
        answer = aaa bbb 11 22 33
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
        