from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        freqs = sorted(cnt.items(), key=itemgetter(1))

        return [n for n, c in freqs[-k:]]