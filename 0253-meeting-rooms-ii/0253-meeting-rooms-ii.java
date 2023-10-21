class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(it -> it[0]));
        
        Queue<int[]> rooms = new PriorityQueue<>(Comparator.comparingInt(it -> it[1]));

        rooms.add(intervals[0]);

        for (int i = 1; i < intervals.length; ++i) {
            var it = intervals[i];
            if (rooms.peek()[1] <= it[0]) {
                rooms.remove();
            }
            rooms.add(it);
        }
        return rooms.size();
    }
}
