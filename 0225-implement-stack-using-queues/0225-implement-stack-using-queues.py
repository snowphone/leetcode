from queue import SimpleQueue

class MyStack:
    def __init__(self):
        self.q = SimpleQueue()
        return

    def push(self, x: int) -> None:
        self.q.put(x)
        return

    def pop(self) -> int:
        new_q = SimpleQueue()
        while self.q.qsize() > 1:
            new_q.put(self.q.get())
        answer = self.q.get()
        self.q = new_q
        return answer

    def top(self) -> int:
        item = self.pop()
        self.push(item)
        return item
        
    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()