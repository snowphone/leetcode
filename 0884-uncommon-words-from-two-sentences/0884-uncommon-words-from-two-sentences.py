from collections import Counter
from itertools import chain

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(
            chain(
                s1.split(' '),
                s2.split(' '),
            )
        )
        return list(
            k for k, v in c.items() if v == 1
        )
    