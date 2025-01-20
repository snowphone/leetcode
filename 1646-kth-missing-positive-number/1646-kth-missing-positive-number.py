from bisect import bisect_right


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        candidate = k
        b, e, delta = 0, len(arr), True
        while delta := bisect_right(arr, candidate, b, e) - b:
            b += delta
            candidate += delta
        return candidate
