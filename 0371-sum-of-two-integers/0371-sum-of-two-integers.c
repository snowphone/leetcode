#define get(n, i) (n & (1L << i))
#define set(n, i) (n | (1L << i))

int getSum(int a, int b) {
    int answer = 0, carry = 0;

    for (int i = 0; i < 32; ++i) {
        int lhs = get(a, i);
        int rhs = get(b, i);

        if (lhs && rhs && carry) {  // Three 1 bits
            answer = set(answer, i);
            carry = 1;
        } else if ((lhs && rhs) || (lhs ^ rhs) && carry) {  // Two 1 bits
            carry = 1;
        } else if ((lhs ^ rhs) || carry) {  // One 1 bit
            carry = 0;
            answer = set(answer, i);
        } else { // Zero 1 bits
            // Do nothing
        }
    }
    return answer;
}