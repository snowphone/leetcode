from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def custom_compare_strings(s1, s2):
            lhs = int(s1 + s2)
            rhs = int(s2 + s1)
            return lhs - rhs

        digits = sorted(
            map(str, nums),
            key=cmp_to_key(custom_compare_strings),
            reverse=True
        )
        if digits and digits[0].startswith('0'):
            return '0'
        return ''.join(digits)