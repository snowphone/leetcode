from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        for k, v in c.items():
            if v >= 3:
                c[k] = 1 if v & 1 else 2
        
        return sum(c.values())