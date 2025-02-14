class ProductOfNumbers:
    def __init__(self):
        self.q = list()
        self.acc_q = [1]
    

    def add(self, num: int) -> None:
        if num == 0:
            self.__init__()
        else:
            self.q.append(num)
            self.acc_q.append(num * self.acc_q[-1])

    def getProduct(self, k: int) -> int:
        if len(self.q) < k:
            return 0
        # a over b
        a = self.acc_q[-1]
        b = self.acc_q[-1-k]
        return a // b


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)