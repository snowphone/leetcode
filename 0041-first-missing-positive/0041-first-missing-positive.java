class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> numset = Arrays.stream(nums)
                .filter(it -> it > 0)
                .boxed()
                .collect(Collectors.toSet());
        if (numset.isEmpty() || numset.stream().mapToInt(Integer::valueOf).min().getAsInt() > 1) {
            return 1;
        }
        for (int i = 1; ; i++) {
            if (!numset.contains(i))
                return i;
        }
    }
}