class Logger {
    private HashMap<String, Integer> cache = new HashMap<>();

    public boolean shouldPrintMessage(int timestamp, String message) {
        var before = cache.getOrDefault(message, -987654321);
        if (before + 10 <= timestamp) {
            cache.put(message, timestamp);
            return true;
        }
        return false;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */