class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(it -> it[0]));
        List<int[]> answer = new ArrayList<>();
        answer.add(intervals[0]);


        for (int i = 1; i < intervals.length; i++) {
            var it = intervals[i];
            var last = answer.get( answer.size() - 1 );
            if (last[1] < it[0]) {
                answer.add(it);
                continue;
            }
            last[0] = Math.min(last[0], it[0]);
            last[1] = Math.max(last[1], it[1]);
        }
        return answer.toArray(int[][]::new);
    }
}