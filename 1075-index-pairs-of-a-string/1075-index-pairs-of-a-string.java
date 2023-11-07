class Trie {
	private static final Character TERMINAL = '$';
	private Map<Character, Object> root = new HashMap<>();
	private String needle;

	public Trie(String text) {
		this.needle = text;
	}

	public void add(String word) {
		var nd = root;
		for (var ch : word.toCharArray()) {
			nd.putIfAbsent(ch, new HashMap<Character, Object>());
			nd = (Map<Character, Object>) nd.get(ch);
		}
		nd.put(TERMINAL, new HashMap<Character, Object>());
	}

	public boolean search(int beg, int end) {
		var nd = root;

		for (int i = beg; i < end; ++i) {
			var ch = needle.charAt(i);
			if (!nd.containsKey(ch))
				return false;
			nd = (Map<Character, Object>) nd.get(ch);
		}
		return nd.containsKey(TERMINAL);
	}

	public List<int[]> searchAll(int beg) {
		var nd = root;

		var pairs = new ArrayList<int[]>();

		for (int i = beg; i < needle.length(); ++i) {
			var ch = needle.charAt(i);

			if (nd.containsKey(TERMINAL))
				pairs.add(new int[] {beg, i - 1});

			if (!nd.containsKey(ch))
				return pairs;


			nd = (Map<Character, Object>) nd.get(ch);
		}
		if (nd.containsKey(TERMINAL))
			pairs.add(new int[] {beg, needle.length() - 1});
		return pairs;
	}
}


class Solution {
	public int[][] indexPairs(String text, String[] words) {
		var n = text.length();
		var trie = new Trie(text);

		Arrays.stream(words).forEach(trie::add);

		var answer = new ArrayList<int[]>();
		for (int i = 0; i < n; ++i) {
			answer.addAll(trie.searchAll(i));
		}

		return answer.stream().toArray(int[][]::new);
	}
}