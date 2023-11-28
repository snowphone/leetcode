from operator import mul
from functools import reduce

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_count = corridor.count('S')
        if seat_count & 1 or not seat_count:
            return 0
        
        pairs = self.get_seat_pairs(corridor)
        distances = [pairs[i][0] - pairs[i-1][1] for i in range(1, len(pairs))]

        return reduce(mul, distances, 1) % (10 ** 9 + 7)
        
    def get_seat_pairs(self, corridor: str):
        n = len(corridor)
        answer = []
        i = 0
        while i < n:
            if corridor[i] != 'S':
                i += 1
                continue
            j = next(k for k in range(i+1, n) if corridor[k] == 'S')
            answer.append( (i, j) )
            i = j+1
        return answer