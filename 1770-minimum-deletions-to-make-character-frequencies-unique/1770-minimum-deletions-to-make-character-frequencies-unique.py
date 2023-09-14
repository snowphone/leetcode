from collections import Counter
from operator import itemgetter

class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        cnt = list(map(list, counter.items()))
        cnt.sort(reverse=True, key=itemgetter(1))


        answer = 0
        for i in range(1, len(cnt)):
            ch, n = cnt[i]
            prev_ch, prev_n = cnt[i-1]

            if prev_n > n:
                continue

            if prev_n:
                print(n - prev_n + 1, ch)
                answer += (n - prev_n + 1)
                n -= (n - prev_n + 1)
            else:
                answer += n
                n = 0
            
            cnt[i] = [ch, n]

        return answer


        