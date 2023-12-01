from itertools import chain, zip_longest
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(
            lhs == rhs for lhs, rhs in zip_longest(
                chain(*word1), chain(*word2)
            )
        )