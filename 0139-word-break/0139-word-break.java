class Solution {
    private List<String> words;
    private Map<String, Boolean> cache = new HashMap<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        wordDict.sort(Comparator.naturalOrder());
        this.words = wordDict;

        return tryIt(s);
    }

    private boolean find(String needle) {
        return inner(needle, 0, this.words.size());
    }

    private boolean inner(String needle, int beg, int end) {
        if (end - beg <= 2) {
            return this.words.subList(beg, end).contains(needle);
        }
        int mid = (beg + end) / 2;
        if (needle.compareTo(this.words.get(mid)) < 0)
            return inner(needle, beg, mid);
        else if (this.words.get(mid).compareTo(needle) < 0)
            return inner(needle, mid + 1, end);
        
        return true;
    }

    private boolean tryIt(String s) {
        var cached = this.cache.getOrDefault(s, null);
        if (cached != null)
            return cached;
        
        if (find(s)) {
            this.cache.put(s, true);
            return true;
        }

        for (int i = 1; i < s.length() ; ++i) {
            var head = s.substring(0, i);
            var tail = s.substring(i);
            
            if (find(head) && tryIt(tail)) {
                this.cache.put(s, true);
                return true;
            }
        }
        this.cache.put(s, false);
        return false;
    }
}