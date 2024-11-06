
class Minmax:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max
        return
    
    def __le__(self, other: Self):
        return self.max <= other.min
    
    def update(self, num: int):
        self.min = min(self.min, num)
        self.max = max(self.max, num)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits = [ Minmax(nums[0], nums[0]) ]
        for it in nums[1:]:
            bc = int.bit_count(it)
            if bc == int.bit_count(bits[-1].min):
                bits[-1].update(it)
            else:
                bits.append( Minmax(it, it) )
        
        return all(
            it <= jt for it, jt in zip(bits, bits[1:])
        )
    