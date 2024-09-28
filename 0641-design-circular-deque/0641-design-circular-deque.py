class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.arr = [None] * k
        self.b, self.e = 0, 0
        return
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.b -= 1
        self.arr[self.b] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.e] = value
        self.e += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.b += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.e -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.b]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.e - 1]

    def isEmpty(self) -> bool:
        return self.b == self.e

    def isFull(self) -> bool:
        return self.e - self.b == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
