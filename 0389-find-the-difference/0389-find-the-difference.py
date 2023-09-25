from sortedcontainers import SortedList

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tt = SortedList(t)

        for ch in s:
            tt.remove(ch)
        
        return tt[0]
        