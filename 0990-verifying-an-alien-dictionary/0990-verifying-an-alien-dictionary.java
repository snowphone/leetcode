class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        var dict = new HashMap<Integer, Integer>();

        for (int i = 0; i < order.length(); i++) {
            dict.put(order.codePointAt(i), i);
        }


        var converted = Arrays.stream(words)
                .map(it -> it.chars().map(dict::get).boxed().toList()

                )
                .toList();
        Comparator<List<Integer>> lexicographical = (lhs, rhs) -> {
            var len = Math.min(lhs.size(), rhs.size());

            for (int i = 0; i < len; i++) {
                if (lhs.get(i) == rhs.get(i)) {
                    continue;
                }
                return lhs.get(i) - rhs.get(i);
            }
            return lhs.size() - rhs.size();
        };

        return converted.equals(converted.stream().sorted(lexicographical).toList());
    }
}