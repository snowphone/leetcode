class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = [ [nums[0], nums[0]] ]  # (min, max)
        for it in nums[1:]:
            bc = int.bit_count(it)
            if bc == int.bit_count(bits[-1][0]):
                bits[-1][0] = min(bits[-1][0], it)
                bits[-1][1] = max(bits[-1][1], it)
            else:
                bits.append( [it, it] )
        
        return all(
            it[1] <= jt[0] for it, jt in zip(bits, bits[1:])
        )
    