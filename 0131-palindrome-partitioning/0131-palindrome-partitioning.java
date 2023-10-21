class Solution {
    private HashMap<String, List<List<String>>> cache = new HashMap<>();
    
    public List<List<String>> partition(String s) {
        if (s.length() == 1) {
            return List.of(List.of(s));
        }
        if (cache.containsKey(s)) {
            return cache.get(s);
        }
        List<List<String>> answer = new ArrayList<>();
        if (isPalindrome(s)) {
            answer.add(List.of(s));
        }

        for (int i = 1; i < s.length(); i++) {
            var head = s.substring(0, i);
            if (!isPalindrome(head)) {
                continue;
            }
            var tail = s.substring(i);
            var subanswer = partition(tail);
            for (var sub : subanswer) {
                answer.add(Stream.concat(
                                List.of(head).stream(),
                                sub.stream()
                        ).toList()
                );
            }
        }

        cache.put(s, answer);
        return answer;
    }

    private boolean isPalindrome(String s) {
        var l = 0;
        var r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
