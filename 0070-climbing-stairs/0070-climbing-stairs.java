class Solution {
    private HashMap<Integer, Integer> cache = new HashMap<>();
    public int climbStairs(int n) {
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        var cached = cache.getOrDefault(n, null);
        if (cached != null) {
            return cached;
        }
        
        var answer = climbStairs(n-1) + climbStairs(n-2);
        cache.put(n, answer);
        return answer;
    }
}