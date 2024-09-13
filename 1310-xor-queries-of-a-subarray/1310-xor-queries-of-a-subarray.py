from functools import reduce
import operator

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        return [
            reduce(operator.xor, arr[l:r+1]) for l, r in queries
        ]
        