class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1 = num1.bit_count()
        c2 = num2.bit_count()
        print(c1, c2)

        return self.minimize(num1, c2)
    

    def minimize(self, n, cnt):
        xor = 0
        for i in range(31, -1, -1):
            if ( n & (1 << i) ) and cnt:
                cnt -= 1
                xor |= (1 << i)
        
        if not cnt:
            return xor
        
        for i in range(32):
            if not (n & (1 << i) ) and cnt:
                cnt -= 1
                xor |= (1 << i)
        return xor
