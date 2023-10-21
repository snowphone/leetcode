class MovingAverage {
    Deque<Integer> window = new LinkedList<>();
    int size = 0;
    int sum = 0;
    
    public MovingAverage(int size) {
        this.size = size;
    }

    public double next(int val) {
        if (window.size() == this.size) {
            this.sum -= window.pollFirst();
        }

        window.offerLast(val);
        this.sum += val;
        
        return this.sum / (double) window.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
