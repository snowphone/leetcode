class Solution:
    def totalMoney(self, n: int) -> int:
        acc = 0
        i = 1
        while n:
            first, sz = i, min(7, n)
            acc += sum(range(first, first + sz))

            n -= sz
            i += 1
        return acc



