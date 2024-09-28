from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(it == 0 for it in nums):
            return '0'
            
        def cmp(lhs: int, rhs: int):
            return int(f"{lhs}{rhs}") - int(f"{rhs}{lhs}")

        items = sorted(
            map(str, nums),
            reverse=True,
            key=cmp_to_key(cmp)
        )
        return ''.join(items)
    
