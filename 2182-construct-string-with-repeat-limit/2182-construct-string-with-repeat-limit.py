from collections import Counter
from sortedcontainers import SortedDict


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        q = SortedDict(Counter(s))

        answer = [""]
        while q:
            ch, cnt = q.peekitem(-1)
            if cnt <= repeatLimit:
                answer.append(ch * cnt)
                q.popitem(-1)
                continue
            answer.append(ch * repeatLimit)
            q[ch] -= repeatLimit

            try:
                nxt_ch, nxt_cnt = q.peekitem(-2)
                answer.append(nxt_ch)
                q[nxt_ch] -= 1
                if q[nxt_ch] == 0:
                    del q[nxt_ch]
            except:
                break

        return "".join(answer)
