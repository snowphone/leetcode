class Solution {
    public int buyChoco(int[] prices, int money) {
        int a = 987654321;
        int b = 987654321;
        for (var it: prices) {
            if (it < a) {
                b = a;
                a = it;
                continue;
            }
            if (it < b) {
                b = it;
                continue;
            }
        }

        if (money >= a + b) {
            return money - (a + b);
        }
        return money;
    }
}