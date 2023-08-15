from heapq import *

class Heap(list):
    def __init__(self, ascending=True):
        super().__init__()
        self.sign = 1 if ascending else -1
        return

    def push(self, num):
        heappush(self, num * self.sign)
        return

    def pop(self):
        return self.sign * heappop(self)
    
    def peak(self):
        return self.sign * self[0]
    
class MedianFinder:

    def __init__(self):
        self.left = Heap(ascending=False)
        self.right = Heap()


    def addNum(self, num: int) -> None:
        # Invariant: /\
        if not self.left and not self.right:
            self.left.push(num)
        elif self.findMedian() < num:
            self.right.push(num)
            while len(self.left) < len(self.right):
                tmp = self.right.pop()
                self.left.push(tmp)
        else:
            self.left.push(num)
            # 2 0 -> 1 1
            # 1 0 -> 1 0
            while len(self.left) > len(self.right) + 1:
                tmp = self.left.pop()
                self.right.push(tmp)
        assert len(self.left) in [len(self.right),len(self.right) + 1]
        return
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left.peak() + self.right.peak()) / 2
        return self.left.peak()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()