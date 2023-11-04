class Solution {
	public int getLastMoment(int n, int[] left, int[] right) {
		var answer = new ArrayList<Integer>();

		answer.add(Arrays.stream(left).max().orElse(-1));
		answer.add(n - Arrays.stream(right).min().orElse(n));

		return answer
			.stream()
			.mapToInt(Integer::valueOf)
			.max()
			.orElseThrow();
	}
}