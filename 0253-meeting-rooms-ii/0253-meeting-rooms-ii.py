from operator import itemgetter
from sortedcontainers import SortedList

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=itemgetter(0))

        print(intervals)

        rooms = SortedList([ intervals[0] ], key=itemgetter(1)) 

        for it in intervals[1:]:
            # 맨 앞에 있는 방이 가장 먼저 비워진다.
            # 그러므로 맨 앞방에 새 사람을 앉힐 수 없다면
            # 기존의 방 어디에도 넣을 수 없을 것이다.
            if rooms[0][1] <= it[0]:  # No overlap
                rooms.pop(0)
            rooms.add( it )
        

        return len(rooms)
