from operator import itemgetter
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=itemgetter(0))

        print(intervals)

        answer = []

        while intervals:
            remaining = []
            subanswer = intervals[:1]
            
            for it in intervals[1:]:
                if subanswer[-1][1] <= it[0]:
                    subanswer.append(it)
                else:
                    remaining.append(it)
            answer.append(subanswer)
            intervals = remaining

        return len(answer)
        