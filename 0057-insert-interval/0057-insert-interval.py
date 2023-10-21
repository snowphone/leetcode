class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort()
        answer = [intervals[0]]

        for it in intervals[1:]:
            if answer[-1][1] < it[0]:
                answer.append(it)
                continue
            answer[-1][0] = min(answer[-1][0], it[0])
            answer[-1][1] = max(answer[-1][1], it[1])

        return answer