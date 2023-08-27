class MinStack:
    def __init__(self):
        self.stk = []
        return

    def push(self, val: int) -> None:
        m = min(self.stk[-1][0], val) if self.stk else val
        self.stk.append( (m, val) )

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][1]

    def getMin(self) -> int:
        return self.stk[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()