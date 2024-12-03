from itertools import chain
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        for l, r in zip(
            chain([0], spaces),
            chain(spaces, [len(s)]),
        ):
            words.append(s[l:r])
        return ' '.join(words)