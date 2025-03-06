from collections import Counter
from itertools import chain

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        c = Counter(chain(*grid))

        answer = [None, None]
        for i in range(1, n**2+1):
            if i not in c:
                answer[1] = i
            elif c[i] == 2:
                answer[0] = i
        return answer