class Solution {
    private int[] price;
    private int k;
    
    public int maximumTastiness(int[] price, int k) {
        Arrays.sort(price);
        this.price = price;
        this.k = k;
        
        return narrowDown(0, (int) (Math.pow(10, 9) + 1));
    }
    private int narrowDown(int beg, int end) {
        var sz = end - beg;
        if (sz == 1) {
            return beg;
        }
        int mid = (beg + end) / 2;
        return possible(mid) ? narrowDown(mid, end) : narrowDown(beg, mid);
    }
    
    private boolean possible(int targetTastiness) {
        int lastPrice = this.price[0];
        int answer = 1;
        for (int i = 1; i < this.price.length && answer < this.k; i++) {
            if (this.price[i] - lastPrice < targetTastiness)
                continue;
            lastPrice = this.price[i];
            answer += 1;
        }
        return answer >= this.k;
    } 
}