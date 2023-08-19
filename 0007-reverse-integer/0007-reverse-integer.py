class Solution:
    def to_digits(self, x: int):
        digits = []
        while x:
            digits.append(x % 10)
            x //= 10
        return digits
    
    def to_int(self, digits: list[int]):
        num = 0
        for d in reversed(digits):
            num *= 10
            num += d

        return num
    
    def digit_cmp(self, lhs: list[int], rhs: list[int]):
        return lhs[::-1] < rhs[::-1]

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        digits = self.to_digits(x)
        digits.reverse()
        tmp = sign * self.to_int(digits)
        if -2 ** 31 <= tmp <= 2 ** 31 - 1:
            return tmp
        return 0
        

        