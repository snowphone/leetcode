from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        locs = defaultdict(list)

        for i, ch in enumerate(s):
            locs[ch].append(i)
        
        answer = -1
        for indices in locs.values():
            answer = max(
                answer,
                indices[-1] - indices[0] + 1 - 2,
            )
        return answer

