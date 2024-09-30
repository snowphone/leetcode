from dataclasses import dataclass

@dataclass
class Entry:
    value: int
    inc: int = 0

class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stk: list[Entry] = []

    def push(self, x: int) -> None:
        if len(self.stk) == self.max:
            return
        self.stk.append(Entry(value=x))

    def pop(self) -> int:
        if not self.stk:
            return -1
        entry = self.stk.pop()
        if self.stk:
            self.stk[-1].inc += entry.inc
        return entry.value + entry.inc

    def increment(self, k: int, val: int) -> None:
        end = min(k, len(self.stk))
        self.stk[end-1].inc += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)