class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrset = frozenset(arr)
        def gen():
            i = 1
            while True:
                yield i
                i += 1
        g = gen()
        while k:
            i = next(g)
            if i not in arrset:
                k -= 1
        return i