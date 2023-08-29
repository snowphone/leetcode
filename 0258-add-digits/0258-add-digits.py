class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        acc = 0
        while num:
            acc += (num % 10)
            num //= 10
        return self.addDigits(acc)