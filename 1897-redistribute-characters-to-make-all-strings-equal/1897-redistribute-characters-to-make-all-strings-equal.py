from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter(''.join(words))
        n = len(words)

        return all(
            cnt % n == 0 for cnt in c.values()
        )
        