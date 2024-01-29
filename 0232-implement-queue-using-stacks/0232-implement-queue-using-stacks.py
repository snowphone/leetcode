class MyQueue:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        

    def pop(self) -> int:
        tmp = []
        while self.stk:
            tmp.append(self.stk.pop())
        answer = tmp.pop()
        while tmp:
            self.stk.append(tmp.pop())
        
        return answer
        

    def peek(self) -> int:
        tmp = []
        while self.stk:
            tmp.append(self.stk.pop())
        answer = tmp[-1]
        while tmp:
            self.stk.append(tmp.pop())
        
        return answer
        

    def empty(self) -> bool:
        return not self.stk
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()