from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)

        cnt = 0
        for it in arr:
            if counter[it] == 1:
                cnt += 1
            if cnt == k:
                return it
        return ''