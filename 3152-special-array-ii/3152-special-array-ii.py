class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        specials = ( self.count_not_special(it, jt) for it, jt in zip(nums, nums[1:]) )
        prefix_sum = [0]
        for it in specials:
            prefix_sum.append(it + prefix_sum[-1])

        def get(i: int, j: int):
            '[i, j]'
            return prefix_sum[j] - prefix_sum[i]
            
        return [get(f, t) == 0 for f, t in queries]

    def count_not_special(self, a, b) -> Literal[1, 0]:
        is_odd = lambda n: bool(n & 1)
        special = lambda a, b: is_odd(a) != is_odd(b)
        return 0 if special(a, b) else 1
