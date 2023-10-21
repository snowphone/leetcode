class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        var merged = new ArrayList<int[]>(Arrays.stream(intervals).filter(it -> it[0] < newInterval[0]).toList());
        merged.add(newInterval);
        merged.addAll(
                Arrays.stream(intervals).filter(it -> it[0] >= newInterval[0]).toList()
        );

        var answer = new ArrayList<int[]>();
        answer.add(merged.get(0));

        for (int i = 1; i < merged.size(); ++i) {
            var it = merged.get(i);
            var last = answer.get(answer.size() - 1);
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