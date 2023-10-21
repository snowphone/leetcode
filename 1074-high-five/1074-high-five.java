class Solution {
    public int[][] highFive(int[][] items) {
        var scores = new TreeMap<Integer, ArrayList<Integer>>();
        for (var it : items) {
            var id = it[0];
            var score = it[1];
            var v = scores.getOrDefault(id, new ArrayList<>());
            v.add(score);
            scores.put(id, v);
        }

        var answer = new ArrayList<int[]>();
        for (var it : scores.entrySet()) {
            var id = it.getKey();
            var score = it.getValue().stream().sorted(Comparator.reverseOrder()).limit(5).mapToInt(Integer::intValue).sum() / 5;
            answer.add(new int[]{id, score});
        }
        return answer.toArray(int[][]::new);
    }
}