class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = [str(i) for i in mapping]
        
        return sorted(
            nums,
            key=lambda it: int(''.join((mapping[int(i)] for i in str(it))))
        )