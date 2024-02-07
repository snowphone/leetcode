from collections import Counter
from operator import itemgetter

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([ 
            ch * cnt
            for ch, cnt in sorted(
                Counter(s).items(),
                key=itemgetter(1),
                reverse=True,
            )
        ])