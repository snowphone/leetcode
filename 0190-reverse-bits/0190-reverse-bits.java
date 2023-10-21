public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int answer = 0;
        for (int i = 0; i < 32; ++i) {
            boolean flag =  (n & (1 << i) ) != 0;
            if (flag)
                answer |= (1 << (31 - i) );
        }
        return answer;
    }
}
