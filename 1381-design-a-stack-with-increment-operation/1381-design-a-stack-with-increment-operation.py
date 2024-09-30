class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stk = []

    def push(self, x: int) -> None:
        if len(self.stk) == self.max:
            return
        self.stk.append(x)

    def pop(self) -> int:
        if not self.stk:
            return -1
        return self.stk.pop()

    def increment(self, k: int, val: int) -> None:
        end = min(k, len(self.stk))
        for i in range(0, end):
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)