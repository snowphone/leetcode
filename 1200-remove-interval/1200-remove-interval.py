from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        answer = []

        def overlapped(interval: List[int]):
            return not (interval[1] <= toBeRemoved[0] or toBeRemoved[1] <= interval[0])

        for it in intervals:
            if not overlapped(it):
                answer.append(it)
                continue
            
            if toBeRemoved[0] <= it[0] and it[1] <= toBeRemoved[1]:
                continue  # toBeRemoved is a superset
            if it[0] < toBeRemoved[0] and toBeRemoved[1] < it[1]:
                answer += [
                    [it[0], toBeRemoved[0]],
                    [toBeRemoved[1], it[1]],
                ]
            elif it[0] < toBeRemoved[0]:
                answer.append([it[0], toBeRemoved[0]])
            else:
                answer.append([toBeRemoved[1], it[1]])


        return answer
    