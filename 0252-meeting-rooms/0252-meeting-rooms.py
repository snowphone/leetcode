from operator import itemgetter

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=itemgetter(0))


        return all(
            it[1] <= jt[0] for it, jt in zip(intervals, intervals[1:])
        )


