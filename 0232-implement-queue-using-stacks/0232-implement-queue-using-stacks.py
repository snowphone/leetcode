class MyQueue:

    def __init__(self):
        self.tmp = []
        self.stk = []
        return
        
    def push(self, x: int) -> None:
        self.stk.append(x)
        return

    def pop(self) -> int:
        answer = self.peek()
        self.tmp.pop()
        return answer

    def _move_to_left(self):
        while self.stk:
            self.tmp.append(self.stk.pop())
        return

    def peek(self) -> int:
        if not self.tmp:
            self._move_to_left()
        return self.tmp[-1]
        
    def empty(self) -> bool:
        return not self.stk and not self.tmp
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()