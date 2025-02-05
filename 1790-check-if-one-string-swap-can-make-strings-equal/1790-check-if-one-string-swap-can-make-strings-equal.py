from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffcnt = sum(
            it != jt for it, jt in zip(s1, s2)
        )
        
        return diffcnt in [0, 2] and Counter(s1) == Counter(s2)