from operator import and_
from functools import reduce
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(
            reduce(
                and_,
                map(set, nums),
            )
        )