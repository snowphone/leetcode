from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        q = SortedList()
        for entry in Counter(s).items():
            q.add(entry)
        
        answer = [ '' ]
        while q:
            ch, cnt = q.pop()
            if cnt <= repeatLimit:
                answer.append(ch * cnt)
            else:
                answer.append(ch * repeatLimit )
                remaining = cnt - repeatLimit

                if not q:
                    break
                nxt_ch, nxt_cnt = q.pop()
                answer.append(nxt_ch)
                if nxt_cnt - 1 > 0:
                    q.add((nxt_ch, nxt_cnt - 1))
                q.add((ch, remaining))

        return ''.join(answer)