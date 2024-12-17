from collections import Counter
from heapq import heappush, heappop


class HQ(list):
    def put(self, it):
        fn = lambda jt: (-ord(jt[0]), jt[1])
        heappush(self, (fn(it), it))

    def get(self):
        return heappop(self)[1]


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        q = HQ()
        for entry in Counter(s).items():
            q.put(entry)

        answer = []
        while q:
            ch, cnt = q.get()
            if cnt <= repeatLimit:
                answer.append(ch * cnt)
            else:
                answer.append(ch * repeatLimit)
                remaining = cnt - repeatLimit

                if not q:
                    break
                nxt_ch, nxt_cnt = q.get()
                answer.append(nxt_ch)
                if nxt_cnt - 1 > 0:
                    q.put((nxt_ch, nxt_cnt - 1))
                q.put((ch, remaining))

        return "".join(answer)
