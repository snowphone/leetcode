import operator
from functools import reduce, partial

class ProductOfNumbers:
    prod = partial(reduce, operator.mul)

    def __init__(self):
        self.q = list()
        self.acc_q = [1]

    def add(self, num: int) -> None:
        self.q.append(num)
        self.acc_q.append(num * self.acc_q[-1])

    def getProduct(self, k: int) -> int:
        # a over b
        a = self.acc_q[-1]
        b = self.acc_q[-1-k]
        if b == 0:
            return self.prod(self.q[-k:])
        return a // b


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)