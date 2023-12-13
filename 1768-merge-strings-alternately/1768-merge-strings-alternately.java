class Solution {
	public String mergeAlternately(String word1, String word2) {
		var builder = new StringBuilder();
		var len = Math.min(word1.length(), word2.length());

		for (int i = 0; i < len; i++) {
			builder.append(word1.charAt(i));
			builder.append(word2.charAt(i));
		}

		if (word1.length() > len) {
			builder.append(word1.substring(len));
		} else if (word2.length() > len) {
			builder.append(word2.substring(len));
		}

		return builder.toString();
	}
}