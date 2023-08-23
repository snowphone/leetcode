from collections import Counter, deque
from operator import itemgetter
from heapq import heappush, heappop

class PQ(list):
    def __init__(self, key):
        super().__init__()
        self._key = key
        return
    
    def put(self, item):
        heappush(self, (self._key(item), item) )
    
    def get(self):
        return heappop(self)[1]

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        q = PQ(key=lambda tpl: -tpl[1])

        for it in counter.items():
            q.put(it)
        answer = []
        while len(q) >= 2:
            ch, cnt = q.get()
            ch1, cnt1 = q.get()
            if answer and answer[-1] == ch:
                answer += [ch1, ch]
            else:
                answer += [ch, ch1]

            cnt -= 1; cnt1 -= 1
            if cnt:
                q.put( (ch, cnt) )
            if cnt1:
                q.put( (ch1, cnt1) )

        ans_str = ''.join(answer)
        if not q:
            return ans_str
                
        ch, cnt = q.get()
        if cnt > 1:
            return ''
        if not answer:
            return ch
        elif ch != answer[-1]:
            return ans_str + ch
        elif ch != answer[0]:
            return ch + ans_str
        else:
            return ''

