from functools import cache
from itertools import combinations
from typing import Iterable
from collections import Counter

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()

        def achievable(target_tastiness):
            indices = [0]
            for i in range(1, n):
                if price[i] - price[indices[-1]] < target_tastiness:
                    continue
                indices.append(i)
                if len(indices) >= k:
                    return True
            return False

        beg = 0; end = 10 ** 9 + 1

        while beg + 1 < end:
            mid = (beg + end) // 2
            if achievable(mid):
                beg, end = mid, end
            else:
                beg, end = beg, mid
        return beg
