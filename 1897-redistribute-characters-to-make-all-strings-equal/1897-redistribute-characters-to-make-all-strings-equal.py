from collections import Counter
from itertools import chain
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter(chain(*words))
        n = len(words)

        return all(
            cnt % n == 0 for cnt in c.values()
        )
        