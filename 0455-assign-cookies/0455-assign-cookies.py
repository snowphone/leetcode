from typing import List

from sortedcontainers import SortedList


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        cookies = SortedList(s)

        for greed in g:
            i = cookies.bisect_left(greed)
            if i < len(cookies):
                answer += 1
                del cookies[i]

        return answer